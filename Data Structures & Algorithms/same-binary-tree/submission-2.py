# Definition for a binary tree node.
# class TreeNode:
from types import SimpleNamespace
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True # both empty trees therefore true
        if not p or not q or p.val != q.val: # only one of them is null, they arent the same
            return False 
        # so now p and q are the same! lets do the recursive step
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right)) 
        # if the and is true, we return true, if the and is false, return false



        