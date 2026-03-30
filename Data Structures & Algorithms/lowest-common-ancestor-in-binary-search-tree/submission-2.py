# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#236 Lowest Common ancestor in Binary Seach Tree
# time = o(h) space = o(1)
# 1. Set cur = root.
# 2. While cur is not null:
# 3. If p.val and q.val are both greater than cur.val -> go right.
# 4. Else if both are smaller -> go left.
# 5. Otherwise: You've found the first node where their paths separate -> 5a. return cur (the LCA).
# 6. Return null if tree is empty (should not happen for valid input).

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root  #1

        while cur: #2
            if p.val > cur.val and q.val > cur.val: #3. both greater --> go right
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val: #4. both smaller --> go left
                cur = cur.left
            else: # 5. otherwise: 1st node where paths seperate; return cur
                return cur 