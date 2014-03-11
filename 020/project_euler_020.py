#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_020.py
#
#   Description:  Project Euler, Problem 020
#
#       Created:  Sun 12 Jun 2011 04:31:52 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:25:34 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""Project Euler, Problem 020

n! means n × (n − 1) × ... × 3 × 2 × 1

Find the sum of the digits in the number 100!

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


def n_gt(n):
    if n==0 or n==1:
        return 1
    else:
        return n*n_gt(n-1)

def main(): # main
    start = time.time()

    result = 0
    for i in str(n_gt(100)):
        result += int(i)

    # Print Answer and Time Execute
    print "Answer : ", result
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()
