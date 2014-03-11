#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_022.py
#
#   Description:  Project Euler, Problem 022
#
#       Created:  Sun 12 Jun 2011 04:17:53 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:20:15 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 022

Using names.txt  (right click and 'Save Link/Target As...'), a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each
name, multiply this value by its alphabetical position in the list
to obtain a name score.

For example, when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in
the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
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

    d = {
         'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
         'I': 9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16,
         'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24,
         'Y':25, 'Z':26
        }
    f = open("names.txt", "r")
    data = f.readline().split(",")
    f.close()
    for i in range(0, len(data)):
        data[i] = data[i].strip('"')
    data.sort()
    totalSum = 0
    for i in range(0, len(data)):
        alphaScore = 0
        for j in list(data[i]):
            alphaScore += d[j]
        totalSum += alphaScore*(i+1)

    # Print Answer and Time Execute
    print "Answer : ", totalSum
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()
