"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_pos = height.index(max(height))
        res = 0
        curr_max = 0
        for i in range(0,max_pos):
            if height[i] >= curr_max:
                curr_max = height[i]
            res += curr_max - height[i]
        curr_max = 0
        for i in range(len(height) -1, max_pos, -1):
            if height[i] >= curr_max:
                curr_max = height[i]
            res += curr_max - height[i]
        return res


if __name__ == "__main__":
    c = Solution()
    print(c.trap([0,1,0,2,1,0,1,3,2,1,2,1]))