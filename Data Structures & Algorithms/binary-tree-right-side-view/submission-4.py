# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def rightSide(root, depth):
            if not root:
                return
            if depth == len(res):
                res.append(root.val)
            rightSide(root.right, depth + 1)
            rightSide(root.left, depth + 1)

        rightSide(root, 0)
        return res
            