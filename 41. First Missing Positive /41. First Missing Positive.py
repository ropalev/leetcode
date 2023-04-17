"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums == [1]:
            return 2
        elif len(nums) == 1:
            return 1
        s = dict.fromkeys(range(1, len(nums) + 1))
        for i in nums:
            try:
                del s[i]
            except:
                continue
        return list(s.keys())[0] if s else len(nums) + 1


if __name__ == "__main__":
    c = Solution()
    print(c.firstMissingPositive([2,1]))