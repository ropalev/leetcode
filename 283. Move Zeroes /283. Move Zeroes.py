from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0
        while ptr1 < len(nums) and nums[ptr1] != 0:
            ptr1 += 1
        ptr2 = ptr1 + 1
        while ptr2 < len(nums):
            if nums[ptr2] != 0:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr1 += 1
            ptr2 += 1