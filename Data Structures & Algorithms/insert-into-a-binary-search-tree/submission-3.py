# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            return TreeNode(val)

        def dfs(root):
            nonlocal val
            if not root:
                return
            
            if root.val < val:
                if not root.right:
                    root.right = TreeNode(val)
                    return
                dfs(root.right)
            else:
                if not root.left:
                    root.left = TreeNode(val)
                    return
                dfs(root.left)
        
        dfs(root)
        return root