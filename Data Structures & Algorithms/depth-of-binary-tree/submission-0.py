# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 104 Max Depth of the binary tree----------------
# Strategy: 1. Recursive DFS
# time o(n) space o(h)
#   Best case ( balamced tree)      o(log(n))
#   Worst case (degenerate tree)    o(n)
#   -----------------------------
# 1 . If root is null, return 0.
# 2. Otherwise:
#   a. Recursively compute leftDepth = maxDepth(root.left).
#   b.Recursively compute rightDepth = maxDepth(root.right).
#3. Return 1 + max(leftDepth, rightDepth).
#****************************************************
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
        