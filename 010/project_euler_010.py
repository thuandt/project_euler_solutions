#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_010.py
#
#   Description:  Project Euler, Problem 010
#
#       Created:  Sun 12 Jun 2011 04:17:53 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:23:25 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 010

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import time

__author__ = "Thuan.D.T (MrTux)"
__copyright__ = "Copyright (c) 2011 Thuan.D.T (MrTux)"
__credits__ = ["Thuan.D.T"]
__license__ = "GPLv2"
__version__ = "1.0.0"
__maintainer__ = "MrTux"
__email__ = "mrtux@ubuntu-vn.org"
__status__ = "Release"
__company__ = "Water Resources University (WRU)"


def isPrime(n):
    if ( n < 2 ):
        return False
    elif (n < 4): # 2 and 3 is prime
        return True
    elif (n%2 == 0):
        return False
    elif (n < 9): # we have already excluded 4,6 and 8.
        return True
    elif (n%3 == 0):
        return False
    else:
        i = 5
        while (i*i < n): # sqrt(n) rounded to the greatest integer r so that r*r<=n
            if (n%i == 0):
                return False
            if (n%(i+2) == 0):
                return False
            i += 6
        return True

def main(): # main
    start = time.time()

    result = 0
    i = 1
    while i < 2000000:
        if isPrime(i):
            result += i
        i += 1

    # Print Answer and Time Execute
    print "Answer : ", result
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()

"""Analysis Problem

Some useful facts:
1 is not a prime.
All primes except 2 are odd.
All primes greater than 3 can be written in the form 6k+/-1.
Any number n can have only one primefactor greater than n .
The consequence for primality testing of a number n is: if we cannot
find a number f less than or equal n that divides n then n is prime
the only primefactor of n is n itself
"""
