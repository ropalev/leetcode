"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
"""

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        deepfunc(res,target, path, candidates)
        return res


def deepfunc(res, target, path,candidates):
    if target < 0:
        return
    if target == 0:
        res.append(path.copy())
        return
    for i in range(len(candidates)):
        path.append(candidates[i])
        if candidates[i] <= target:
            deepfunc(res, target - candidates[i], path ,candidates[i:])
        path.pop()

if __name__ == "__main__":
    c = Solution()
    candidates = [1,2,3,4,5,6,7]
    target = 9
    print(c.combinationSum(candidates,target))