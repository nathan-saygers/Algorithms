#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n >= 3:
    return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
  if n == 2:
    return eating_cookies(n - 2) + eating_cookies(n - 1)
  if n < 2 and n > -1:
    return 1

# 1 => 1 (1)
# 2 => 2 (1 * 2, 2 * 1)
# 3 => 4 (1 * 3, 2 * 1 + 1 * 1,  1 * 1 +2 * 1,  3 * 1)
# 4 => 5 (4 * 1, 1 * 4, 2 * 2, 3 * 1 + 1, 1 * 3 + 1, 
#
#

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')