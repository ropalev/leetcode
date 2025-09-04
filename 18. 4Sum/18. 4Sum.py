class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def kSum(nums,target, k):
            res = []
            if not nums:
                return res
            average_value = target // k
            if average_value < nums[0] or nums[-1] < average_value:
                return res
            if k==2:
                return twoSum(nums,target)

            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for subset in kSum(nums[i + 1 :], target - nums[i], k - 1):
                        res.append([nums[i]] + subset)

            return res

        def twoSum(nums, target):
            res = []
            l, r = 0, len(nums)-1
            while l < r:
                s = nums[l]+nums[r]
                if s >target or (r<len(nums)-1 and nums[r]==nums[r+1]):
                    r -=1
                elif s < target or (l>0 and nums[l]==nums[l-1]):
                    l+=1
                else:
                    res.append([nums[l],nums[r]])
                    l+=1
                    r -=1
                    while l<r and nums[l]==nums[l-1]:l+=1
                    while l<r and nums[r]==nums[r+1]: r-=1
            return res



        return kSum(nums, target, 4)