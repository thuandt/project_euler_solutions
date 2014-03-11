#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_005.py
#
#   Description:  Project Euler, Problem 005
#
#       Created:  Sun 12 Jun 2011 04:39:32 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:25:53 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 005

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

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


def gcd(a, b):
    """GCD = Greatest Common Divisor
    import fractions : to use gcd built in fuctions
    http://en.wikipedia.org/wiki/Greatest_common_divisor
    Euclid Algorithm : http://en.wikipedia.org/wiki/Euclidean_algorithm
    same gcd built-in fuction of module fractions base on Euclidean algorithm
    """
    while b:
        a, b = b, a%b
    return a

def lcm(a,b):
    """LCM = Least Common Multiple
    Dựa vào liên hệ giữa LCM và GCD
    http://en.wikipedia.org/wiki/Least_common_multiple
    """
    return (a/gcd(a, b))*b


def main(): # main
    start = time.time()

    result = reduce(lcm, range(2, 20))
    # reduce : http://docs.python.org/library/functions.html#reduce

    # Print Answer and Time Execute
    print "Answer : ", result
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()

"""Analysis Problem

See more at pdf file
"""
