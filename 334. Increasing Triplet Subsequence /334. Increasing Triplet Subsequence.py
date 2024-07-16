from typing import List
from functools import reduce
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_nums = []
        max_nums = []
        for i, n in enumerate(nums):
            if not min_nums:
                min_nums.append(nums[i])
                max_nums.append(nums[-i-1])
                continue
            min_nums.append(min(min_nums[-1], nums[i]))
            max_nums.append(max(max_nums[-1], nums[-i-1]))
        max_nums = max_nums[::-1]
        for i in range(len(nums)):
            if min_nums[i] < nums[i] < max_nums[i]:
                return True
        return False

if __name__ == "__main__":
    print(Solution().increasingTriplet([1,5,0,4,1,3]))
    print(Solution().increasingTriplet([-1,1,0,-3,3]))
    print(Solution().increasingTriplet([1,2,3,4,5]))
