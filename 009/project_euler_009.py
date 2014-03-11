#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_009.py
#
#   Description:  Project Euler, Problem 009
#
#       Created:  Sun 12 Jun 2011 04:17:53 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:09:50 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 009

A Pythagorean triplet is a set of three natural numbers is :
        a < b < c, for which, a^(2) + b^(2) = c^(2)

For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
 
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
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


def main(): # main
    start = time.time()

    c = 0
    for a in range(1, 1000):
        for b in range(1000-a, 1, -1):
            c = 1000-a-b
            if (a < b) and (c > 0):
                if a**2 + b**2 == c**2 :
                    result = a*b*c

    # Print Answer and Time Execute
    print "Answer : ", result
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()

