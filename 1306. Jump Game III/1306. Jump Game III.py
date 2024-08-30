"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.

Notice that you can not jump outside of the array at any time.
"""

from typing import List
import queue as q
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        qq = q.Queue()
        dp = [0 for i in range(len(arr))]
        dp[start] = 1
        qq.put(start)
        while not qq.empty():
            idx = qq.get()
            if idx < len(arr) and not arr[idx]:
                return True
            if idx - arr[idx] >= 0 and not dp[idx-arr[idx]]:
                qq.put(idx - arr[idx])
                dp[idx-arr[idx]] = 1
            if idx + arr[idx] < len(arr) and not dp[idx+arr[idx]]:
                qq.put(idx + arr[idx])
                dp[idx+arr[idx]] = 1
        return False


c = Solution().canReach(arr = [3,0,2,1,2], start = 2)
print(c)
