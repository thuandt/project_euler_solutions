#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_034.py
#
#   Description:  Project Euler, Problem 034
#
#       Created:  Sun 12 Jun 2011 04:17:53 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:00:42 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 034

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their
digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
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

    fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880) # 1! to 9!
    result = 0
    for n in range(10, 50000):
      x = sum(fact[int(d)] for d in str(n))
      if n == x:
          result += n

    # Print Answer and Time Execute
    print "Answer : ", result
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()


"""Analysis Problem

These type of numbers are referred to as factorions and it’s easy to learn that
only 4 exist: 1, 2, 145 & 40585. The problem description wants us to ignore
1 & 2 so the answer to this problem should become obvious.

But, let’s write a program anyway to search for factorions. As usual, when
writing a brute force search algorithm, we must first determine our bounds. The
lower bound is 10 because single digit candidates are to be ignored. The upper
bound we discover as follows (from Wikipedia):

If n is a natural number of d digits that is a factorion, then 10d − 1 ≤ n ≤ 9!d
and this fails to hold for d ≥ 8. Thus n has 7 digits and the maximum sum of
factorials of digits for a 7 digit number is 9!7 = 2,540,160, which is the upper
bound.

Afterwards, we learned 50,000 worked just fine.
"""
