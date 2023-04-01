from typing import  List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    l += 1
                    res = min(res, s, key= lambda x: abs(target -x))
                elif s > target:
                    r -= 1
                    res = min(res, s, key=lambda x: abs(target - x))
                else:
                    return s

        return res


if __name__ == "__main__":
    nums, target = input().split(" ")
    target = int(target)
    nums = list(map(int, nums.split(",")))

    c = Solution()
    print(c.threeSumClosest(nums, target))