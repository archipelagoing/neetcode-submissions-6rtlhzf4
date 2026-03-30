# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#----25. Invert Binary Tree-----⋆౨ৎ˚⟡˖ ࣪-----------------------
#2. DFS Attempt: level by level traversal----⋆౨ৎ˚⟡˖ ࣪---------
#   a. If the current node is null, return null.
#   b. Swap the node's left and right pointers.
#   c. Recursively call dfs on the new left child.
#   d. Recursively call dfs on the new right child.
#   e. Return the current node (now inverted).
#---⋆౨ৎ˚⟡˖ ࣪Time Complexxity: o(n)--⋆౨ৎ˚⟡˖--࣪Space Complexxity: o(n)----


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root