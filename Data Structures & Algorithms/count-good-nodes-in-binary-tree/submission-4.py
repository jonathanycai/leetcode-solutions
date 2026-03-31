# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, root, maxSeen):
        if root == None:
            return 0

        res = 0
        if root.val >= maxSeen:
            res += 1
            print(root.val)
        
        maxSeen = max(maxSeen, root.val)

        res += self.dfs(root.left, maxSeen)
        res += self.dfs(root.right, maxSeen)

        return res