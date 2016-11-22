# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""
A class for calculating business date deltas based on a policy.

Definitions:

    Weekend - a day off reoccurring on a weekly basis (no shifting weekends
    supported)

    Holiday - a special day off. The app is agnostic as to how holidays reoccur.
    It expects a list of date instances that represent a sequence of holidays
    within the desired range.

    Policy - a definition of weekends and holidays.

"""

from datetime import datetime, time, timedelta

__version__ = '0.2.0'

MON = 0
TUE = 1
WED = 2
THU = 3
FRI = 4
SAT = 5
SUN = 6


def set_time(day, hour):
    """Set the time of the day to the given hour."""
    return day.replace(hour=hour.hour, minute=hour.minute, second=hour.second)


class Policy(object):
    """
    Policy class defined holidays and weekends. All calculations related to
    business day arithmetics are done in teh context of Policy.
    """

    def __init__(self, weekends=None, holidays=None, hours=None):
        """Initialise the class.

        Args:
            weekends: list or tuple, a days to consider in the weekend.
            holidays: list or tuple, all the holidays.
            hours: list or tuple of datetime.time, when work begins and ends during a day.
        """
        if len(weekends) > 6:
            raise AssertionError("Too many weekends per week")
        if hours is not None and len(hours) != 2:
            raise AssertionError("Working hours must specify a beginning and an end")
        self.weekends = weekends or []
        self._holidays = []
        self._set_holidays(holidays)
        self.hours = hours

    def _get_holidays(self):
        return self._holidays

    def _set_holidays(self, holidays):
        if holidays:
            self._holidays = list(holidays)
            self._holidays.sort()
        else:
            self._holidays = []

    holidays = property(_get_holidays, _set_holidays)

    def is_empty(self):
        """ Returns True is policy has no weekends or holidays.

        >>> policy = Policy()
        >>> policy.is_empty()
        True
        >>> policy = Policy(weekends=[SUN,])
        >>> policy.is_empty()
        False
        """
        return not (self.weekends or self._holidays)

    def is_weekend(self, day):
        """ Returns True only if the day falls on a weekend.

        >>> policy = Policy(weekends=(SAT, SUN))
        >>> policy.is_weekend(date(2011, 7, 1)) # Friday
        False
        >>> policy.is_weekend(date(2011, 7, 2)) # Saturday
        True
        >>> policy.is_weekend(date(2011, 7, 3)) # Sunday
        True
        >>> policy.is_weekend(date(2011, 7, 4)) # Monday
        False
        """
        return day.weekday() in self.weekends

    def is_holiday(self, day):
        """ Returns true only if the day falls on a holiday.
        >>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,  7,  1),))
        >>> policy.is_holiday(date(2011, 7, 1)) # Friday
        True
        >>> policy.is_holiday(date(2011, 7, 2)) # Saturday
        False
        """
        return day in self._holidays

    def is_day_off(self, day):
        """ Returns True if the day is either weekend or holiday.

        >>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,  7,  1), ))
        >>> policy.is_day_off(date(2011, 7, 1)) # Friday
        True
        >>> policy.is_day_off(date(2011, 7, 2)) # Saturday
        True
        >>> policy.is_day_off(date(2011, 7, 3)) # Sunday
        True
        >>> policy.is_day_off(date(2011, 7, 4)) # Monday
        False
        """
        return self.is_weekend(day) or self.is_holiday(day)

    def is_not_in_business_hours(self, day):
        """ Returns if the datetime is not in business hours.

        >>> policy = Policy(hours=(time(8, 30), time(20, 30)))
        >>> policy.is_not_in_business_hours(datetime(2011, 7, 1, 8, 0, 0))
        True
        >>> policy.is_not_in_business_hours(datetime(2011, 7, 1, 15, 0, 0))
        False
        """
        if self.hours is None:
            return False

        if self.hours[0] < self.hours[1]:
            return day.time() < self.hours[0] or day.time() > self.hours[1]
        else:
            return day.time() < self.hours[0] and day.time() > self.hours[1]

    def closest_biz_day(self, day, forward=True):
        """If the given date falls on a weekend or holiday, returns the closest
        business day. Otherwise the original date is returned. If forward is
        True (default) the returned date will be next closest business date.
        Otherwise closest previous business date will be retured.

        It does not check for the hour.

        >>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,  7,  1), ))
        >>> policy.closest_biz_day(date(2011, 6, 30)) # regular business day
        datetime.date(2011, 6, 30)
        >>> policy.closest_biz_day(date(2011, 7, 1)) # Friday of long weekend
        datetime.date(2011, 7, 4)
        >>> policy.closest_biz_day(date(2011, 7, 1), False) # Previous closest buisuness day
        datetime.date(2011, 6, 30)
        """

        if forward:
            delta = timedelta(days=1)
        else:
            delta = timedelta(days=-1)
        while day.weekday() in self.weekends or day in self.holidays:
            day = day + delta
        return day

    def holidays_between(self, day1, day2, skip_weekends=True):
        """
        Returns the number of holidays between two given dates, excluding
        boundaries. If skip_weekends is True (default) holidays occuring on
        weekends will not be counted.

        >>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,  7,  1), date(2011, 8, 1)))
        >>> policy.holidays_between(date(2011, 6, 12), date(2011, 9, 12))
        2
        >>> policy.holidays_between(date(2011,  7,  1), date(2011, 8, 1))
        0
        """

        if day1 > day2:
            return self.holidays_between(day2, day1)
        if day1 == day2:
            return 0
        if isinstance(day1, datetime):
            day1 = day1.date()
        if isinstance(day2, datetime):
            day2 = day2.date()

        n = 0
        # FIXME: should probably use bisect here
        for h in self._holidays:
            if h > day1:
                if h >= day2:
                    break
                if skip_weekends:
                    if h.weekday() not in self.weekends:
                        n += 1
                else:
                    n += 1
        return n

    def add_seconds(self, day, seconds):
        """Adds the given seconds to the day.

        It is mainly intended as a helper for the add function but can be called from outside.

        Args:
            day: datetime.datetime, the given day.
            seconds: integer, the number of seconds to add.

        >>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,7,1)), hours=(time(8), time(20)))
        >>> day = datetime(2011, 6, 30, 14, 30)
        >>> policy.add_seconds(day, 3600) # One hour after
        datetime.datetime(2011, 6, 30, 15, 30)
        >>> policy.add(day, 36000) # The next working day
        datetime.datetime(2011, 7, 4, 12, 30)
        """
        if self.hours is None:
            if self.is_day_off(day):
                day = set_time(day, time())
            return self.closest_biz_day(day + timedelta(seconds=seconds))

        begin_hours = self.hours[0]
        end_hours = self.hours[1]

        # Put us in business hours
        if self.is_day_off(day):
            day = set_time(day, begin_hours)
            day = self.closest_biz_day(day, forward=True)

        elif self.is_not_in_business_hours(day):
            if day.time() > begin_hours:
                day += timedelta(days=1)
            day = set_time(day, begin_hours)

        # Fill the current day
        end_of_day = set_time(day, end_hours)
        if day.time() > end_hours:
            end_of_day += timedelta(days=1)
        seconds_in_day = (end_of_day - day).seconds

        if seconds <= seconds_in_day:
            # All the seconds are in the current day
            return day + timedelta(seconds=seconds)
        else:
            # Move to next day
            if not (day.time() < begin_hours):
                day += timedelta(days=1)
            next_day = set_time(day, begin_hours)
            return self.add_seconds(next_day, seconds - seconds_in_day)

    def add_days(self, day, days):
        """Adds the given number of days.

        Args:
            day: datetime.datetime, the given day.
            days: integer, the number of days to add, possibly negative.

        >>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,7,1), date(2011,8,1)))
        >>> day = date(2011, 6, 29) # Wednesday
        >>> policy.add_days(day, 2) # Monday after the long weekend
        datetime.date(2011, 7, 4)
        >>> policy.add_days(day, 22) # Spanning two holidays and several weekends
        datetime.date(2011, 8, 2)
        >>> policy.add_days(day, 10, reverse=True) # 10 business days (2 weeks) ago
        datetime.date(2011, 6, 15)
        """
        if days < 0:
            sign = -1
            look_forward = False
        else:
            sign = 1
            look_forward = True

        if self.weekends:
            weeklen = 7 - len(self.weekends)
            weeks_add = abs(days) // weeklen * sign
            days_add = abs(days) % weeklen * sign
        else:
            weeks_add = 0
            days_add = days

        new_date = day + timedelta(days=weeks_add * 7)
        while days_add:
            # remaining days may or may not include weekends;
            new_date = new_date + timedelta(sign)
            if not self.is_weekend(new_date):
                days_add -= 1

        days_add = self.holidays_between(day, new_date)  # any holidays?
        if days_add:
            return self.add(new_date, days_add * sign)
        else:
            return self.closest_biz_day(new_date, look_forward)

    def add(self, day, delta):
        """Adds a timedelta to the day, taking care of business days.

        Delta should be a timedelta object, possibly negative.
        For backwards compatibility, it can also be an integer representing a number of days.

        >>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,7,1), date(2011,8,1)))
        >>> day = date(2011, 6, 29) # Wednesday
        >>> policy.add(day, timedelta(days=2)) # Monday after the long weekend
        datetime.date(2011, 7, 4)
        >>> policy.add(day, timedelta(days=22)) # Spanning two holidays and several weekends
        datetime.date(2011, 8, 2)
        >>> policy.add(day, timedelta(days=10), reverse=True) # 10 business days (2 weeks) ago
        datetime.date(2011, 6, 15)

        >>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,7,1)), hours=(time(8), time(20)))
        >>> day = datetime(2011, 6, 29, 14, 30)
        >>> policy.add(day, timedelta(days=1, hours=5)) # The day after, in the afternoon
        datetime.datetime(2011, 6, 29, 19, 30)
        >>> policy.add(day, timedelta(days=1, hours=10)) # Too many hours, will finish the monday after the long weekend
        datetime.datetime(2011, 7, 4, 12, 30)
        """

        if isinstance(delta, int):
            delta = timedelta(days=delta)

        if isinstance(day, datetime):
            # Add hours only if the given day is a datetime
            day = self.add_seconds(day, delta.seconds)

        return self.add_days(day, delta.days)

    def weekends_between(self, day1, day2):
        """
        Returns the number of weekends between two dates, including upper boundary.

        >>> policy = Policy(weekends=(SAT, SUN))
        >>> policy.weekends_between(date(2011, 6, 3), date(2011, 6, 15))
        4
        >>> policy.weekends_between(date(2011, 6, 4), date(2011, 6, 11)) # SAT to SAT
        2
        """

        # FIXME: check about boundaries
        if day2 < day1:
            return self.weekends_between(day2, day1)
        delta = day2 - day1
        weeks = delta.days // 7
        extra = delta.days % 7
        n = weeks * len(self.weekends)
        while extra:
            day = day2 - timedelta(days=extra)
            if self.is_weekend(day):
                n += 1
            extra -= 1
        return n

    def biz_day_delta(self, day1, day2):
        """
        Returns the number of business days between day1 and day2, excluding
        boundaries.

        >>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,  7,  1),))
        >>> policy.biz_day_delta(date(2011, 7, 4), date(2011, 6, 30)) # one holiday, one weekend between
        1
        >>> policy.biz_day_delta(date(2011, 6, 10), date(2011, 6, 24), ) # two weekends between
        10
        """
        if day2 < day1:
            return self.biz_day_delta(day2, day1)

        delta = day2 - day1

        return delta.days - self.weekends_between(day1, day2) - self.holidays_between(day1, day2)


if __name__ == "__main__":
    # run tests when called directly
    import doctest
    doctest.testmod()
