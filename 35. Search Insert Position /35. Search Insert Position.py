"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

"""
[4,8,10,15,20], 30
mid = 2
10 < 30
l =2 r = 5
mid = 3
15 < 30
l = 3 r = 5
 mid = 4
20 < 30
l =4 r = 5
mid = 4



[1,3,5,7,9,10] 0
0 5
mid = 2
0 3
mid = 1
0 2
mid = 1

"""

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (r+l) //2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        return l if nums[l] >= target else l+1

if __name__ == "__main__":
    c = Solution()
    print(c.searchInsert(nums = [1] , target = 1))