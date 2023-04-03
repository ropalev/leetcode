"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""

"""
nums = [2,5,6,0,0,1,2], target = 0
"""

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) -1
        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            mid = (l+r) // 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid -1
                else:
                    l = mid +1

            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1
        return False




if __name__ == "__main__":
    nums = [1,0,1,1,1]
    target = 0
    c = Solution()
    print(c.search(nums,target))