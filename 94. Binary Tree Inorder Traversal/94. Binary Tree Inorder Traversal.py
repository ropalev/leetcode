# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        dfs(root,res)
        return res

def dfs(node, res):
    if node:
        dfs(node.left,res)
        res.append(node.val)
        dfs(node.right, res)

