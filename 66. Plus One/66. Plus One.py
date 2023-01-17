from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(c) for c in str(int("".join((str(i) for i in digits)))+1)]

if __name__ == '__main__':
    c = Solution()
    print(c.plusOne([1,2,3]))
    print(c.plusOne([9,9,9]))