#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      Filename:  project_euler_003.py
#
#   Description:  Project Euler, Problem 003
#
#       Created:  Sun 12 Jun 2011 04:17:53 AM ICT
# Last Modified:  Sun 12 Jun 2011 05:15:09 AM ICT
#
#        Author:  Thuan.D.T (MrTux)
#       Company:  Water Resources University (WRU)
#     Copyright:  (c) 2011, MrTux <mrtux@ubuntu-vn.org>

"""ProjectEuler, Problem 003

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import time, math

__author__ = "Thuan.D.T (MrTux)"
__copyright__ = "Copyright (c) 2011 Thuan.D.T (MrTux)"
__credits__ = ["Thuan.D.T"]
__license__ = "GPLv2"
__version__ = "1.0.0"
__maintainer__ = "MrTux"
__email__ = "mrtux@ubuntu-vn.org"
__status__ = "Release"
__company__ = "Water Resources University (WRU)"


top_number = 600851475143

def zero_mod(divisor):
    if top_number % divisor == 0:
        return True
    else:
        return False

def is_prime(divided):
    divisor = 3
    sqrt_divided = math.sqrt(divided)
    if divided == 1:
        return True
    else:
        while divisor <= sqrt_divided:
            if divided == divisor:
                return True
            elif divided % divisor == 0:
                return False
            else:
                divisor += 2
        return True

def main(): # main
    start = time.time()

    count = 3
    go_to = top_number
    first_list =[]
    while count <= go_to:
        if zero_mod(count):
            first_list.append(count)
            go_to = top_number / count
            first_list.append(go_to)
        count += 2
    second_list = map(is_prime, first_list)
    result = max(zip(second_list, first_list))[-1]


    # Print Answer and Time Execute
    print "Answer : ", result
    print "Time   : ", str(time.time() - start)
    return 0

if __name__ == '__main__':
    print __doc__
    main()
