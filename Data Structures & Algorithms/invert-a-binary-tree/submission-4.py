# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return

        
        left = self.invertTree(root.left) #recursively visit left and right child
        right = self.invertTree(root.right)

        #to set pointer of current root, do root.(left, right) = (where you want to set it to)

        root.left = right
        root.right = left

        return root
        

        