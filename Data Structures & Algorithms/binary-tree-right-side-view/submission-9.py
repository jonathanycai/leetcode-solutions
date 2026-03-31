# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res, 0)
        return res

    def dfs(self, node, res, currHeight):
        if not node:
            return
        
        if currHeight == len(res):
            res.append(node.val)
        
        self.dfs(node.right, res, currHeight + 1)
        self.dfs(node.left, res, currHeight + 1)