class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        curr_min = prices[0]
        global_min = 0
        for i in range(len(prices)):
            profit = prices[i] - curr_min
            curr_min = min(curr_min, prices[i])
            global_min = max(profit, global_min)
        return global_min