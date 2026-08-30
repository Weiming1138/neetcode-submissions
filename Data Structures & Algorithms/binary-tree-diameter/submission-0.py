# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0 #what i will return

        def dfs(curr): #returns height, not diameter
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right) #left + right is finding diameter, compare it to result and update it
            return max(left, right) + 1 #max of either subtree + 1 for max of height from current
        
        dfs(root)
        return self.res
        



        
            