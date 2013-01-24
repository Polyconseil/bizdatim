#!/usr/bin/env python

import unittest
from datetime import date, datetime, time, timedelta
from bizdatetime import Policy, MON, TUE, WED, THU, FRI, SAT, SUN

holidays = (
    date(2009, 12, 25), # xmas
    date(2009, 12, 28), # boxing day in on
    date(2010,  1,  1), # new year
    date(2010,  2, 15), # family day
    date(2010,  4,  2), # April 2. Good Friday
    date(2010,  5, 24), # May 24. Victoria Day
    date(2010,  7,  1), # July 1. Canada Day
    date(2010,  8,  2), # August 2. Civic Holiday
    date(2010,  9,  6), # September 6. Labour Day
    date(2010, 10, 11), # October 11. Thanksgiving Day
    date(2010, 12, 27), # December 27. Christmas Day
    date(2010, 12, 28), # December 28. Boxing Day
    date(2011,  1,  3), # moves to Monday
    date(2011,  2, 21), # February 21. Family Day
    date(2011,  4, 22), # Good Friday
    date(2011,  5, 23), # Victoria Day
    date(2011,  7,  1), # Canada Day
    date(2011,  8,  1), # Civic Holiday
    date(2011,  9,  5), # Labour Day
    date(2011, 10, 10), # October 10. Thanksgiving Day
    date(2011, 12, 26), # December 26. Christmas Day
    date(2011, 12, 27), # December 27. Boxing Day
)


class TestAddition(unittest.TestCase):

    def test_add_days(self):
        policy = Policy(weekends=(SAT, SUN), holidays=holidays)
        self.assertEqual(policy.add(date(2011, 3, 3), 1), date(2011, 3, 4))
        self.assertEqual(policy.add(date(2011, 3, 3), 2), date(2011, 3, 7))
        self.assertEqual(policy.add(date(2011, 3, 3), 3), date(2011, 3, 8))
        self.assertEqual(policy.add(date(2011, 3, 3), 4), date(2011, 3, 9))
        self.assertEqual(policy.add(date(2011, 3, 3), 5), date(2011, 3, 10))
        self.assertEqual(policy.add(date(2011, 3, 3), 6), date(2011, 3, 11))
        self.assertEqual(policy.add(date(2011, 3, 3), 7), date(2011, 3, 14))
        self.assertEqual(policy.add(date(2011, 3, 3), 8), date(2011, 3, 15))
        self.assertEqual(policy.add(date(2011, 3, 3), 9), date(2011, 3, 16))
        self.assertEqual(policy.add(date(2011, 3, 3), 10), date(2011, 3, 17))
        self.assertEqual(policy.add(date(2011, 3, 3), 11), date(2011, 3, 18))
        self.assertEqual(policy.add(date(2011, 3, 3), 12), date(2011, 3, 21))
        self.assertEqual(policy.add(date(2011, 3, 3), 13), date(2011, 3, 22))
        self.assertEqual(policy.add(date(2011, 3, 3), 14), date(2011, 3, 23))
        self.assertEqual(policy.add(date(2011, 3, 3), 15), date(2011, 3, 24))
        self.assertEqual(policy.add(date(2011, 3, 3), 16), date(2011, 3, 25))
        self.assertEqual(policy.add(date(2011, 3, 3), 17), date(2011, 3, 28))
        self.assertEqual(policy.add(date(2011, 3, 3), 18), date(2011, 3, 29))
        self.assertEqual(policy.add(date(2011, 3, 3), 19), date(2011, 3, 30))
        self.assertEqual(policy.add(date(2011, 3, 3), 20), date(2011, 3, 31))
        self.assertEqual(policy.add(date(2011, 3, 3), 21), date(2011, 4, 1))
        self.assertEqual(policy.add(date(2011, 3, 3), 22), date(2011, 4, 4))
        self.assertEqual(policy.add(date(2011, 3, 3), 23), date(2011, 4, 5))
        self.assertEqual(policy.add(date(2011, 3, 3), 24), date(2011, 4, 6))
        self.assertEqual(policy.add(date(2011, 3, 3), 25), date(2011, 4, 7))
        self.assertEqual(policy.add(date(2011, 3, 3), 26), date(2011, 4, 8))
        self.assertEqual(policy.add(date(2011, 3, 3), 27), date(2011, 4, 11))
        self.assertEqual(policy.add(date(2011, 3, 3), 28), date(2011, 4, 12))
        self.assertEqual(policy.add(date(2011, 3, 3), 29), date(2011, 4, 13))
        self.assertEqual(policy.add(date(2011, 3, 3), 30), date(2011, 4, 14))
        self.assertEqual(policy.add(date(2011, 3, 3), 31), date(2011, 4, 15))
        self.assertEqual(policy.add(date(2011, 3, 3), 32), date(2011, 4, 18))
        self.assertEqual(policy.add(date(2011, 3, 3), 33), date(2011, 4, 19))
        self.assertEqual(policy.add(date(2011, 3, 3), 34), date(2011, 4, 20))
        self.assertEqual(policy.add(date(2011, 3, 3), 35), date(2011, 4, 21))
        self.assertEqual(policy.add(date(2011, 3, 3), 36), date(2011, 4, 25))
        self.assertEqual(policy.add(date(2011, 3, 3), 37), date(2011, 4, 26))
        self.assertEqual(policy.add(date(2011, 3, 3), 38), date(2011, 4, 27))
        self.assertEqual(policy.add(date(2011, 3, 3), 39), date(2011, 4, 28))
        self.assertEqual(policy.add(date(2011, 3, 3), 40), date(2011, 4, 29))

    def test_negative_addition(self):
        pass

    def test_add_seconds(self):
        begin = time(8, 30)
        end = time(20, 30)
        policy = Policy(weekends=(SAT, SUN), holidays=holidays, working_hours=(begin, end))
        # Nominal
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 3, 8, 30), 3600), datetime(2011, 3, 3, 9, 30))
        # Before begin
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 3, 7, 30), 3600), datetime(2011, 3, 3, 9, 30))
        # Day before
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 2, 22, 30), 3600), datetime(2011, 3, 3, 9, 30))
        # Many hours
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 3, 6, 30), 50400), datetime(2011, 3, 4, 10, 30))
        # During weekend
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 5, 10, 30), 3600), datetime(2011, 3, 7, 9, 30))
        # Span weekend
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 4, 15, 30), 36000), datetime(2011, 3, 7, 13, 30))

    def test_add_seconds_no_working_hours(self):
        policy = Policy(weekends=(SAT, SUN), holidays=holidays, working_hours=None)
        # Nominal
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 3, 8, 30), 3600), datetime(2011, 3, 3, 9, 30))
        # During weekend
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 5, 10, 30), 3600), datetime(2011, 3, 7, 1, 0))
        # Span weekend
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 4, 20, 30), 36000), datetime(2011, 3, 7, 6, 30))

    def test_add_seconds_night_shift(self):
        begin = time(8, 30)
        end = time(20, 30)
        policy = Policy(weekends=(SAT, SUN), holidays=holidays, working_hours=(end, begin))
        # Nominal
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 3, 5, 30), 3600), datetime(2011, 3, 3, 6, 30))
        self.assertEqual(policy.add_seconds(datetime(2011, 3, 2, 22, 30), 10800), datetime(2011, 3, 3, 1, 30))

    def test_add(self):
        begin = time(8, 30)
        end = time(20, 30)
        policy = Policy(weekends=(SAT, SUN), holidays=holidays, working_hours=(begin, end))
        # Nominal, just days
        self.assertEqual(policy.add(datetime(2011, 3, 3, 8, 30), timedelta(days=1)), datetime(2011, 3, 4, 8, 30))
        self.assertEqual(policy.add(datetime(2011, 3, 3, 8, 30), timedelta(days=2)), datetime(2011, 3, 7, 8, 30))
        # Just days, non working hours
        self.assertEqual(policy.add(datetime(2011, 3, 3, 6, 30), timedelta(days=2)), datetime(2011, 3, 7, 8, 30))
        # Nominal
        self.assertEqual(policy.add(datetime(2011, 3, 3, 8, 30), timedelta(days=2, hours=3)),
            datetime(2011, 3, 7, 11, 30))
        # Too many hours
        self.assertEqual(policy.add(datetime(2011, 3, 3, 8, 30), timedelta(days=2, hours=15)),
            datetime(2011, 3, 8, 11, 30))


class TestNonWorkingHours(unittest.TestCase):

    def test_no_working_hours(self):
        policy = Policy(weekends=(SAT, SUN), holidays=holidays)
        self.assertFalse(policy.is_non_working_hours(time(19, 25)))

    def test_normal_hours(self):
        begin = time(8, 30)
        end = time(20, 30)
        policy = Policy(weekends=(SAT, SUN), holidays=holidays, working_hours=(begin, end))
        self.assertTrue(policy.is_non_working_hours(datetime(2011, 7, 1, 7, 0)))
        self.assertFalse(policy.is_non_working_hours(datetime(2011, 7, 1, 17, 0)))
        self.assertFalse(policy.is_non_working_hours(datetime(2011, 7, 1, 8, 30)))

    def test_night_shift(self):
        begin = time(8, 30)
        end = time(20, 30)
        policy = Policy(weekends=(SAT, SUN), holidays=holidays, working_hours=(end, begin))
        self.assertFalse(policy.is_non_working_hours(datetime(2011, 7, 1, 7, 0)))
        self.assertTrue(policy.is_non_working_hours(datetime(2011, 7, 1, 17, 0)))
        self.assertFalse(policy.is_non_working_hours(datetime(2011, 7, 1, 8, 30)))


if __name__ == '__main__':
    unittest.main()
