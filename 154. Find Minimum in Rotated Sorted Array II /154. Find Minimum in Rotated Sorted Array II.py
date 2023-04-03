"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

    [4,5,6,7,0,1,4] if it was rotated 4 times.
    [0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
"""


from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        if r ==0:
            return nums[0]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r =  mid if nums[r] != nums[mid] else r - 1
        return nums[r]

"""
l,r = 0, 6
mid = 3
4 < 7
r = 2
l,r = 0,2
mid = 1
1 < 4
r = 0
0,0
mid = 0
r = -1
nums[mid] = nums[l] = 0

[4,5,6,7,0,1,4]
l,r = 0, 6
mid = 3
7 > 4 True
l,r = 4,6
mid = 5
1>4 False
l,r = 4, 5
mid = 4
0 > 1 False
l r = 4 4

r = -3

[-1,1,2,3,-2]
l,r = 0,4
mid = 2
2 > -2 True
l,r = 3,4
mid = 3
3> -2
l,r = 4,4
mid = 4
r = 3

[3,1,1]
l,r = 0,2
mid = 1
1 > 1 False
l,r = 2,2
mid = 2
1>1 False
l,r = 2,1
3,1,3,3
l r = 0 3
mid =1
1 > 3 False
l r = 0 1
mid = 1
1>1 FAlse
l r = 0 0

[3,1]
l r = 0 1
mid = 0 
3 > 1 True
l r = 1 1
mid = 1
1 > 1 False
l r = 1
"""
if __name__ == "__main__":
    nums =  [3,1,3,3]

    c = Solution()
    print(c.findMin(nums))