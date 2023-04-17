"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""

from typing import List


class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = abs(n)
        res = 1
        while n:
            if n % 2:
                res = res * x
            x = x * x
            n = n // 2
        return res



if __name__ == "__main__":
    c = Solution()
    print(c.myPow(2,7))