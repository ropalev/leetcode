class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([1 for i in S if i in J])