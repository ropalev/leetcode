"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = 0
        max_jump = 0
        while j <= max_jump:
            max_jump = max(j + nums[j], max_jump)
            if max_jump >= len(nums) - 1:
                return True
            j += 1
        return False


if __name__ == "__main__":
    c = Solution()
    print(c.canJump([2,0,1,0]))