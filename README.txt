ABOUT
=====

python-bizdatetime is a simple library for performing business day arithmetic.


KNOWN LIMITATIONS
=================

Rotating weekends/holidays are not supported (e.g., two days working, third day
off).

Business hour arithmetic is not (yet) supported.


DEFINITIONS
===========

Weekend
    Weekly repeating non-business day. Weekend does not have to be at the end
    (or beginning) or the week. Weekends do not have to be consecutive days.

Holiday
    Like weekend, holiday is a non-business day. Unlike weekend, holiday does
    not have weekly regularity. It is just a date. Holiday can coincide with
    weekend.

Policy
    Is a (possibly empty) collection of holidays and holidays. All calculations
    are performed within a policy.


SAMPLE USAGE
============

All business day arithmetic is performed in the context of policy::
    
    from bizdatetime import *
    from datetime import date
    policy = Policy(weekends=(SAT, SUN), holidays=(date(2011,7,1),))
    day = date(2011, 6, 29) # Wednesday
    print policy.add(day, 2) # add 2 business dates -> Monday after the long weekend
    print policy.biz_day_delta(date(2011, 7, 4), date(2011, 6, 30)) # one holiday, one weekend between

The output of the above program will be::

    datetime.date(2011, 7, 4)
    1

Policy method docstrings contain more examples.
