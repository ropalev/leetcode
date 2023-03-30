"""
Given a string s, find the length of the longest
substring
without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 0
        max_len = 0
        while right != len(s):
            sub_s = s[left:right]
            if len(sub_s) == len(set(sub_s)):
                max_len = max_len if max_len > len(sub_s) else len(sub_s)
                right += 1
            else:
                left += 1
        while left != right:
            sub_s = s[left:right]
            if len(sub_s) == len(set(sub_s)):
                max_len = max_len if max_len > len(sub_s) else len(sub_s)
            left += 1
        return max_len


if __name__ == '__main__':
    c = Solution()
    s = input()
    print(c.lengthOfLongestSubstring(s))
