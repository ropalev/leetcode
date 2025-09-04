class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_set = nums
        result = []
        res_dict = {}
        def backtrack(position):
            if position==len(nums)-1:
                if not res_dict.get(tuple(nums)):
                    result.append(nums[:])
                    res_dict[tuple(nums)] = True
                return
            for i in range(position, len(nums)):
                nums[position], nums[i] = nums[i], nums[position]
                backtrack(position+1)
                nums[position], nums[i] = nums[i], nums[position]
        backtrack(0)
        return result