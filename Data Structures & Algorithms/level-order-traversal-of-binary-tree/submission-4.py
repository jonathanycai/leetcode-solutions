# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        res = []
        q.append(root)

        while q:
            curr = []
            length = len(q)
            for _ in range(length):
                node = q.popleft()
                q.append(node.left) if node.left else None
                q.append(node.right) if node.right else None
                curr.append(node.val)
            res.append(curr)
        
        return res

