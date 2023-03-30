"""
Given a string s, return the longest
palindromic
substring
in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i, _ in enumerate(s):
            odd = PalyndromFindLen(s, i, i)
            even = PalyndromFindLen(s, i, i + 1)
            res = max(res, odd, even, key=len)
        return res

def PalyndromFindLen(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

if __name__ == "__main__":
    s = input()
    c = Solution()
    print(c.longestPalindrome(s))