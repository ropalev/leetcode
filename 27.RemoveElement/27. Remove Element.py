from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        filter_len = len(filter_nums := list(filter(lambda x: x != val, nums)))
        nums[0: filter_len] = filter_nums
        return filter_len
        
if __name__ == '__main__':
    c = Solution()
    nums = [3,2,2,3]
    print(c.removeElement(nums, 3))
    print(nums)