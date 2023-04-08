"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping
intervals that cover all the intervals in the input.
"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        inter = sorted(intervals, key=lambda x: x[0])
        inter.append([float("inf"), float("inf")])
        left, right = None, None
        res = []
        for i in inter:
            if left is None:
                left = i[0]
                right = i[1]
            elif i[0] <= right:
                right = i[1] if i[1] > right else right
            elif i[0] > right:
                res.append([left, right])
                left = i[0]
                right = i[1]
        return res
if __name__ == "__main__":
    c = Solution()
    print(c.merge([[1,4],[2,3]]))