#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_007.py
#
#   Description:  Project Euler, Problem 007
#
#       Created:  Sun 12 Jun 2011 04:54:03 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:26:19 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 007

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?

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
        while (i*i <= n): # sqrt(n) rounded to the greatest integer r so that r*r<=n
            if ( n%i == 0 ):
                return False
            if ( n%(i+2) == 0 ):
                return False
            i += 6
        return True

def main(): # main
    start = time.time()

    count = 0
    i = 1
    result = 0
    while count <= 10001:
        if isPrime(i):
            count += 1
            if count == 10001:
                result = i
        i += 1

    # Print Answer and Time Execute
    print "Answer : ", result
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()
