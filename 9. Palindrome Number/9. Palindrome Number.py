class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        s_rev = s[::-1]
        return s == s_rev


if __name__ == '__main__':
    c = Solution()
    print(c.isPalindrome(1211))