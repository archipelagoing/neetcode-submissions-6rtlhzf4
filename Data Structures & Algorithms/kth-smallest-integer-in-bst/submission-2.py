# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root 

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right



 
"""
alright so  lets talk about the implementation of iterative dfs
 stack --> push all the left nodes ( as deep as possible)
        - pop the top node ( next smallest value)
        - move to its right subtree & repeat

        ok i did solve this problem but i dont remember how it works

"""
        