"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for r in range(1,m):
            obstacleGrid[r][0] = int((obstacleGrid[r-1][0] == 1) and (obstacleGrid[r][0] == 0))
        for c in range(1, n):
            obstacleGrid[0][c] = int((obstacleGrid[0][c-1] == 1) and (obstacleGrid[0][c] == 0))
        for r in range(1,m):
            for c in range(1,n):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = obstacleGrid[r-1][c] + obstacleGrid[r][c-1]
        return obstacleGrid[m-1][n-1]
        # for i in range(len(obstacleGrid[0])):
        #     for j in range(len(obstacleGrid)):
        #         if i == 0 or j == 0:
        #             dp[i][j] = 1 if dp[i][j] != "X" else 0
        #         else:
        #             if dp[i][j] != "X":
        #
        #                 dp[i][j] = dp[i-1][j] if dp[i-1][j] != "X" else 0

if __name__ == "__main__":
    c = Solution()
    obstacleGrid = [[0,1],[0,0]]
    print(c.uniquePathsWithObstacles(obstacleGrid))