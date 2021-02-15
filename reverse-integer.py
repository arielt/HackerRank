# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range
# [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers
# (signed or unsigned).

# Runtime: 16 ms, faster than 88.85% of Python online submissions
# for Reverse Integer.
# Memory Usage: 13.4 MB, less than 40.68% of Python online submissions
# for Reverse Integer.


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = abs(x)
        r = 0

        while y > 0:
            t = y % 10
            y = y/10
            r = r*10 + t

        if r > 2147483647:
            return 0

        if x < 0:
            r = -r

        return r

