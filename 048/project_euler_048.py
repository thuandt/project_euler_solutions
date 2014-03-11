#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_048.py
#
#   Description:  Project Euler, Problem 048
#
#       Created:  Sun 12 Jun 2011 04:50:09 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:26:10 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 048

The series, 1^(1) + 2^(2) + 3^(3) + ... + 10^(10) = 10405071317.

Find the last ten digits of the series
1^(1) + 2^(2) + 3^(3) + ... + 1000^(1000).

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

    result = 0
    for i in range(1, 1000):
        result += i**i

    # Print Answer and Time Execute
    print "Answer : ", str(result)[-10:]
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()
