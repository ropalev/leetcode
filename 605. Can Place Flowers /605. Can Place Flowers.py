from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def check(i):
            if len(flowerbed) == 1:
                if flowerbed[i] == 0:
                    return True
                return False
            if i == 0:
                return not (flowerbed[i] or flowerbed[i+1])
            elif i == len(flowerbed) - 1:
                return not (flowerbed[i-1] or flowerbed[i])
            return not (flowerbed[i] or flowerbed[i+1] or flowerbed[i-1])
        if not n:
            return True

        for i, f in enumerate(flowerbed):
            if check(i):
                n -= 1
                flowerbed[i] = 1
            if not n:
                return True
        return False



if __name__ == "__main__":
    print(Solution().canPlaceFlowers([1,0], n = 0))