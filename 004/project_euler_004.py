#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_004.py
#
#   Description:  Project Euler, Problem 004
#
#       Created:  Sun 12 Jun 2011 04:17:53 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:12:13 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 004

A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
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


def isPalindromic(n):
    numList=str(n)
    if (numList == numList[::-1]):
        return True
    return False

def main(): # main
    start = time.time()

    maxNumber = 0
    a = 999
    while (a >= 100):
        if (a%11 == 0):
            b  = 999
            db = 1
        else:
            b  = 990
            db = 11
        while (b >= a):
            if (a*b <= maxNumber):
                break
            if isPalindromic(a*b):
                maxNumber = a*b
            b -= db
        a -= 1

    # Print Answer and Time Execute
    print "Answer : ", maxNumber
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()


"""Analysis Problem
The palindrome can be written as:
abccba

Which then simpifies to:
100000a + 10000b + 1000c + 100c + 10b + a

And then:
100001a + 10010b + 1100c

Factoring out 11, you get:
11(9091a + 910b + 100c)

So the palindrome must be divisible by 11. Seeing as 11 is prime, at least
one of the numbers must be divisible by 11. So brute force in Python,
only with less numbers to be checked:
"""
