"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        oldToNew = {}

        def dfs(root):
            if root in oldToNew:
                return oldToNew[root]
            
            newNode = Node(root.val)
            oldToNew[root] = newNode

            for n in root.neighbors:
                newNode.neighbors.append(dfs(n))
            
            return newNode

        dfs(node)
        return oldToNew[node]