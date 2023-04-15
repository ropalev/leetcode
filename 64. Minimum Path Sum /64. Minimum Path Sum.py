"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        w,h = len(grid[0]), len(grid)
        for i in range(1,w):
            grid[0][i] += grid[0][i-1]
        for i in range(1,h):
            grid[i][0] += grid[i-1][0]
        for i in range(1,h):
            for j in range(1,w):
                grid[i][j] = min(grid[i][j] + grid[i-1][j], grid[i][j] + grid[i][j-1])
        return grid[-1][-1]

if __name__ == "__main__":
    c = Solution()
    print(c.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
