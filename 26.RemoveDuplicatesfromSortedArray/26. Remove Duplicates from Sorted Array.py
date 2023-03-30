from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[0:len(dict.fromkeys(nums).keys())] = dict.fromkeys(nums).keys()
        return len(dict.fromkeys(nums).keys())


if __name__ == '__main__':
    c = Solution()
    print(c.removeDuplicates([1,1,2]))
    print(c.removeDuplicates([1,1,2,3,4,4]))
    print(c.removeDuplicates([1,1,2,5,6,7]))