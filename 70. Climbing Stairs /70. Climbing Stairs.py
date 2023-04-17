"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2,len(dp)) :
            dp[i] += dp[i-1] + dp[i-2]
        return dp[-1]

if __name__ == "__main__":
    c = Solution()
    print(c.climbStairs(3))