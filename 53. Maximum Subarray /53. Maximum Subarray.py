"""
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.
"""


"""
-2  1 -3  4 -1  2 1 -5  4
 0  0 -2  2  3  5 6  1  5 5
 [-2,1,-3,4,-1,2,1,-5,4]
"""
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_array = [0] * (len(nums) + 1)
        mmax = float("-inf")
        for i in range(1, len(max_array)):

            max_array[i] = max(max_array[i - 1]+ nums[i-1], nums[i-1])
            mmax = max(mmax, max_array[i])
        return mmax

if __name__ == "__main__":
    c = Solution()
    print(c.maxSubArray([-1]))