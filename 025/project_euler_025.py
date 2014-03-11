#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_025.py
#
#   Description:  Project Euler, Problem 025
#
#       Created:  Sun 12 Jun 2011 04:17:53 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:25:44 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 025

The Fibonacci sequence is defined by the recurrence relation:
F_(n) = F_(n−1) + F_(n−2), where F_(1) = 1 and F_(2) = 1.

Hence the first 12 terms will be:

F_(1) = 1
F_(2) = 1
F_(3) = 2
F_(4) = 3
F_(5) = 5
F_(6) = 8
F_(7) = 13
F_(8) = 21
F_(9) = 34
F_(10) = 55
F_(11) = 89
F_(12) = 144

The 12th term, F_(12), is the first term to contain three digits.
What is the first term in the Fibonacci sequence to contain 1000 digits?
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

    a, b, count = 0, 1, 0
    while len(str(b)) < 1000:
        count+=1
        a, b = b, a+b

    # Print Answer and Time Execute
    print "Answer : ", count+1
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()
