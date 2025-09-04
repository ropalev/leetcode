class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtraking(position):
            if position ==len(nums)-1:
                result.append(nums[:])
                return
            for i in range(position,len(nums)):
                nums[i], nums[position] = nums[position], nums[i]
                backtraking(position+1)
                nums[position], nums[i] = nums[i], nums[position]
        backtraking(0)
        return result