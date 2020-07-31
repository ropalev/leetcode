class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        res = [] * len(candies)
        for k in candies:
            if k + extraCandies >= max_value:
                res.append(True)
            else:
                res.append(False)
        return res