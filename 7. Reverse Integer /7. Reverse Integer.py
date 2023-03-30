"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        num = str(x).rstrip("0")
        minus_flag = num[0] == "-"
        if minus_flag:
            num = num[1:]
        res = -int(num[::-1]) if minus_flag else int(num[::-1])
        if res > 2 **31 -1 or res < -2 ** 31:
            res = 0
        return res

if __name__ == "__main__":
    num = int(input())
    c = Solution()
    print(c.reverse(num))
