# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preidx, self.inidx = 0, 0

        def dfs(limit):
            if self.preidx == len(preorder):
                return
            
            if inorder[self.inidx] == limit:
                self.inidx += 1
                return None
            
            root = TreeNode(preorder[self.preidx])
            self.preidx += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)

            return root
        
        return dfs(float("inf"))