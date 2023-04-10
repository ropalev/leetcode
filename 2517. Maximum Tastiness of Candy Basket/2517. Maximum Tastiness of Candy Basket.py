"""
You are given an array of positive integers price where price[i] denotes the price of the ith candy and a positive integer k.

The store sells baskets of k distinct candies. The tastiness of a candy basket is the smallest absolute difference of the prices of any two candies in the basket.

Return the maximum tastiness of a candy basket.
"""

from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        l,r = 0, sum(price)
        while l < r:
            mid = (l + r) // 2
            if check(mid, (price,k)):
                l = mid + 1
            else:
                r = mid
        return r -1

def check(value, params):
    k, price = params[1], params[0]
    last, count, i = price[0],1,1
    while count < k and i < len(price):
        if price[i] - last >= value:
            last, count = price[i], count + 1
        i += 1
    return count == k

if __name__ == "__main__":
    c = Solution()
    print(c.maximumTastiness(price = [1,3,1], k = 2))
