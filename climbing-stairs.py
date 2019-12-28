# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        
        res = [None] * max(n, 2)
        res[0] = 1
        res[1] = 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[n-1]

