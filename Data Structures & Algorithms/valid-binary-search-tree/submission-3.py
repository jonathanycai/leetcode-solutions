# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, l, r):
            if root == None:
                return True
            
            if root.val > l and root.val < r:
                left = dfs(root.left, l, root.val)
                right = dfs(root.right, root.val, r)
                return right and left
            
            return False
        
        return dfs(root, float("-inf"), float("inf"))