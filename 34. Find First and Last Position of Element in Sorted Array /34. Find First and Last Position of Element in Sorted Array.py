"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""



"""
1,1,2,3,4,4,5,6,7,8,9    4
l r = 0 10
mid = 5
l r = 0 5
mid = 2
l r = 1 5
mid = 3
l r = 2 5
mid = 3


1 1 1 1 1 1 1 1 1 1
l r = 0 9
mid = 4
l r = 0 4
mid = 2
l r = 0 2
mid = 1
l r = 0 1
mid = 0
l r = 0 0



1 2 3 4 5 6 6 6 6 6 7 8 9
l r = 0 12
mid = 6
l r = 6
mid = 3
l r = 2 6
mid = 4
l r = 3 6

"""

from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0,len(nums) -1
        flag = False
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                flag = True
                r = mid -1
                continue
            if nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        left = l if flag else -1
        flag = False
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                l = mid + 1
                flag = True
                continue
            if nums[mid] > target:
                r = mid -1
            else:
                l = mid + 1
        right = r if flag else -1
        return left, right

if __name__ == "__main__":
    c = Solution().searchRange
    print(c([-1,1,1,1,2], 0))