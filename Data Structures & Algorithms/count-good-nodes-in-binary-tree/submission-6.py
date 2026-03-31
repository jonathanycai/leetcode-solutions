# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, greatestSoFar):
            nonlocal res

            if node == None:
                return
            
            if node.val >= greatestSoFar:
                res += 1
                greatestSoFar = node.val
            
            dfs(node.left, greatestSoFar)
            dfs(node.right, greatestSoFar)
        
        dfs(root, root.val)
        return res