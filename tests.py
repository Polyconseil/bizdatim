#!/usr/bin/env python

import unittest
from datetime import date
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
    
    def setUp(self):
        self.policy = Policy(weekends=(SAT, SUN), holidays=holidays)

    def test_positive_addition(self):
        self.assertEqual(self.policy.add(date(2011, 3, 3), 1), date(2011, 3, 4))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 2), date(2011, 3, 7))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 3), date(2011, 3, 8))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 4), date(2011, 3, 9))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 5), date(2011, 3, 10))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 6), date(2011, 3, 11))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 7), date(2011, 3, 14))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 8), date(2011, 3, 15))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 9), date(2011, 3, 16))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 10), date(2011, 3, 17))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 11), date(2011, 3, 18))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 12), date(2011, 3, 21))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 13), date(2011, 3, 22))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 14), date(2011, 3, 23))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 15), date(2011, 3, 24))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 16), date(2011, 3, 25))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 17), date(2011, 3, 28))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 18), date(2011, 3, 29))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 19), date(2011, 3, 30))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 20), date(2011, 3, 31))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 21), date(2011, 4, 1))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 22), date(2011, 4, 4))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 23), date(2011, 4, 5))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 24), date(2011, 4, 6))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 25), date(2011, 4, 7))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 26), date(2011, 4, 8))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 27), date(2011, 4, 11))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 28), date(2011, 4, 12))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 29), date(2011, 4, 13))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 30), date(2011, 4, 14))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 31), date(2011, 4, 15))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 32), date(2011, 4, 18))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 33), date(2011, 4, 19))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 34), date(2011, 4, 20))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 35), date(2011, 4, 21))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 36), date(2011, 4, 25))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 37), date(2011, 4, 26))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 38), date(2011, 4, 27))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 39), date(2011, 4, 28))
        self.assertEqual(self.policy.add(date(2011, 3, 3), 40), date(2011, 4, 29))
    
    def test_negative_addition(self):
        pass

if __name__ == '__main__':
    unittest.main()
