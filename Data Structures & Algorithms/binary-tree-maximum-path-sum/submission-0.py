# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            #a. compute max path with split , making sure not negative
            res[0] = max(res[0], root.val + leftMax + rightMax)
            # b. No split? pick the larger value, leftMax or rightMax
            return root.val + max(leftMax,rightMax)
        
        dfs(root)
        return res[0]


"""
4dx
- the path sum = sum of all node values in the path. 
- i want the LARGEST path sum
- well if its a binary tree, is it also sorted so that all the largest nodes are on the right? no
- at any node, we can only split once. 
-    so starting at the root, we're gonna try to see what the maximum path we can get without splitting
so dont we just want to keep seeing what the highest nmode is, left or right
-  
"""
        