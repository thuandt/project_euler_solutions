#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_001.py
#
#   Description:  Project Euler, Problem 001
#
#       Created:  Sun 12 Jun 2011 03:44:42 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:04:05 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 001

if we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
multiples of 3 or 5 below 1000.
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


limit = 999

def SumDivisibleBy(n):
    p = limit/n
    return n*(p*(p+1))/2

def main(): # main
    start = time.time()

    result = SumDivisibleBy(3) + SumDivisibleBy(5) - SumDivisibleBy(15)

    # Print Answer and Time Execute
    print "Answer : ", result
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()

"""Analysis Problem

But wait a minute: if we had asked to do the same for all numbers less than
1,000,000,000 that is going to take quite a while. Perhaps you would like to try
out that first (make sure your sum variable does not overflow).

To get a more efficient solution you could also calculate the sum of the numbers
less than 1000 that are divisible by 3, plus the sum of the numbers less
than1000 that are divisible by 5. But as you have summed numbers divisible by 15
twice you would have to subtract the sum of the numbers divisible by 15.

If we now define a function:

Function SumDivisibleBy(n)
      Details to be filled in
EndFunction

Then the answer would be :

SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)

Let’s look at the details of our function and take as example n=3.
We would have to add:
    3+6+9+12+......+999=3*(1+2+3+4+...+333)
For n=5 we would get:
    5+10+15+...+995=5*(1+2+....+199)

Now note that 199=995/5 but also 999/5 rounded down to the nearest integer. If
we now also note that 1+2+3+...+p=1⁄2*p*(p+1) our program becomes:

target=999
Function SumDivisibleBy(n)
   p=target div n
   return n*(p*(p+1)) div 2
EndFunction
Output SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)

See more at 001_overview.pdf

"""
