class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dct = {}
        for i in nums:
            dct[i] = dct.get(i,0) + 1
        summ = 0
        for k,v in dct.items():
            summ += v*(v-1)//2
        return summ
