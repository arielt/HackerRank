# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting
# with any positive integer, replace the number by the sum of the
# squares of its digits, and repeat the process until the number equals
# 1 (where it will stay), or it loops endlessly in a cycle which does #
# not include 1. Those numbers for which this process ends in 1 are 
# happy numbers.

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n not in seen:
            seen.add(n)
            res = 0
            while n > 0:
                res += (n % 10) ** 2
                n /= 10
            if res == 1:
                return True
            n = res
        return False

