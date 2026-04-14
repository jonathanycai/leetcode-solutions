# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                rep = root.right
                while rep.left:
                    rep = rep.left
                
                tmpRight = root.right
                tmpLeft = root.left
                root = TreeNode(rep.val)
                root.left = tmpLeft
                root.right = tmpRight

                root.right = self.deleteNode(root.right, rep.val)
        
        return root
