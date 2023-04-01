"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        parenthesis = ""
        add_parhentess(0, 0, n, parenthesis, res)
        return res


def add_parhentess(left, right, n, parenthesis, res):
    if len(parenthesis) == n * 2:
        res.append(parenthesis)
        return
    if left < n:
        add_parhentess(left + 1, right, n,parenthesis+ '(', res)

    if right < left:
        add_parhentess(left, right + 1, n,parenthesis + ')', res)


if __name__ == "__main__":
    n = int(input())
    depth = 0

    res = []

    print(res)