from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        res = [1] * num_len
        p = 1
        for i in range(num_len):
            res[i] = p
            p *= nums[i]
        p = 1
        for i in range(num_len - 1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res


if __name__ == "__main__":
    print(Solution().productExceptSelf([1,2,3,4]))
    print(Solution().productExceptSelf([-1,1,0,-3,3]))