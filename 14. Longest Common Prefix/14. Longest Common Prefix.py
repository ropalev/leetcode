import os
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)

if __name__ == '__main__':
    c = Solution