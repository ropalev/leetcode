"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.
"""

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        if sum(candidates) == target:
            return [candidates]
        candidates.sort()
        res = []
        path = []
        used = set()
        deepfunc(res, target, path, candidates,0)
        return list(set(res))

def deepfunc(res, target, path, candidates, start):
    if target < 0:
        return
    if target == 0:
        res.append(tuple(sorted(path)))
        return
    for i in range(start,len(candidates)):
        if i > start and candidates[i] == candidates[i- 1]:
            continue
        if candidates[i] > target:
            break
        deepfunc(res, target - candidates[i], path + [candidates[i]], candidates, i+1)



if __name__ == "__main__":
    c = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(c.combinationSum2(candidates,target))