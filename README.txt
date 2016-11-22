ABOUT
=====

bizdatim is a simple library for performing business day arithmetic.


KNOWN LIMITATIONS
=================

Rotating weekends/holidays are not supported (e.g., two days working, third day
off).

The business hour arithmetic is limited to additions.


DEFINITIONS
===========

Weekend
    Weekly repeating non-business day. Weekend does not have to be at the end
    (or beginning) or the week. Weekends do not have to be consecutive days.

Holiday
    Like weekend, holiday is a non-business day. Unlike weekend, holiday does
    not have weekly regularity. It is just a date. Holiday can coincide with
    weekend.

Working hours
    The starting and ending time of a business day.

Policy
    Is a (possibly empty) collection of weekends, holidays and working hours. All calculations
    are performed within a policy.


SAMPLE USAGE
============

All business day arithmetic is performed in the context of policy::
    
>>> from bizdatim import Polycy, SAT, SUN
>>> from datetime import date
>>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,7,1),))
>>> day = date(2011, 6, 29) # Wednesday
>>> print policy.add(day, 2) # add 2 business dates -> Monday after the long weekend
datetime.date(2011, 7, 4)
>>> print policy.biz_day_delta(date(2011, 7, 4), date(2011, 6, 30)) # one holiday, one weekend between
1

There is also the possibility to do arithmetic on business hours::
>>> policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,7,1)), hours=(time(8), time(20)))
>>> day = datetime(2011, 6, 29, 14, 30)
>>> policy.add(day, timedelta(days=1, hours=5)) # The day after, in the afternoon
datetime.datetime(2011, 6, 29, 19, 30)
>>> policy.add(day, timedelta(days=1, hours=10)) # Too many hours, will finish the monday after the long weekend
datetime.datetime(2011, 7, 4, 12, 30)

Policy method docstrings contain more examples.
