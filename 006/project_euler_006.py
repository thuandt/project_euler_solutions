#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_006.py
#
#   Description:  Project Euler, Problem 006
#
#       Created:  Sun 12 Jun 2011 04:17:53 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:03:25 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 006

The sum of the squares of the first ten natural numbers is:
    1^(2) + 2^(2) + ... + 10^(2) = 385

The square of the sum of the first ten natural numbers is:
    (1 + 2 + ... + 10)^(2) = 55^(2) = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
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

    result = 100*(100**2 - 1) * (3*100 + 2) / 12

    # Print Answer and Time Execute
    print "Answer : ", result
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()



"""Analysis Problem

A = (1 + 2 + ... + n)^2 = n^2 * (n+1)^2 * 1/4

B = 1^2 + 2^2 + ... + n^2 = n * (n+1) * (2n+1) * 1/6

C = A - B = n * (n^2 - 1) * (3n + 2) * 1/12

"""
