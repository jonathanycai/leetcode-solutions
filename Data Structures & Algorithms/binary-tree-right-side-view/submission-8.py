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

    def dfs(self, root, res, depth):
        if not root:
            return

        if depth == len(res):   
            res.append(root.val)

        self.dfs(root.right, res, depth + 1)
        self.dfs(root.left, res, depth + 1)