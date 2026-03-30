# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#----25. Invert Binary Tree-----⋆౨ৎ˚⟡˖ ࣪-----------------------
# 1. Breadth First Search Attempt------⋆౨ৎ˚⟡˖ ࣪----------------
# a. If the tree is empty, you should return null
# b. Initialize a queue & insert the root node
# c. While the queue is not empty:
#   c1. Remove the front node.
#   c2. Swap its left & right child
#   c3. If left child exists, add it to the queue
#   c4. If right child exists, add it to the queue
# d. After all nodes are processed, return the root as the inverted tree.
#---⋆౨ৎ˚⟡˖ ࣪Time Complexxity: o(n)--⋆౨ৎ˚⟡˖--࣪Space Complexxity: o(n)----------

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if not root: # a. If the tree is empty, you should return null
        #     return None
        # queue = dequeue([root]) # b. Initialize a queue & insert the root node
        # while queue: # c. While the queue is not empty:
        #     node = queue.popleft()
        #     node.left,node.right = node.right, node.left
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        # return root  

        if not root:# a. if the tree is empty, return null
            return None
        queue = deque([root]) #b. initialize a que & insert the root node # its called deque not dequeue kms
        while queue: #c. while the queue isnt empty
            node = queue.popleft() # c1. remove front node 
            node.left, node.right = node.right,node.left # c2. swap the left child & right child
            if node.left: # c3. if there is a left node (old right node), add that first to the queue
                queue.append(node.left)
            if node.right: # c4. if there is a right node ( old left node), add that 2nd to the queue
                queue.append(node.right)

        return root # d. After all nodes are processed, return root as the inverted tree