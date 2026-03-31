# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        if root:
            q.append(root)
        res = []

        while q:
            level = []
            size = len(q)
            for _ in range(size):
                currNode = q.popleft()
                if currNode:
                    if currNode.left:
                        q.append(currNode.left)
                    if currNode.right:
                        q.append(currNode.right)
                    level.append(currNode.val)
            res.append(level)
        
        return res
        