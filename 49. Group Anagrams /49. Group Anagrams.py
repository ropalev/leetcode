"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            res[''.join(sorted(s))] = res.get(''.join(sorted(s)),[]) + [s]
        return [v for v in res.values()]


if __name__ == "__main__":
    c = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(c.groupAnagrams(strs))