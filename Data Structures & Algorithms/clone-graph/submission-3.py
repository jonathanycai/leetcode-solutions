"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        if not node:
            return None

        def dfs(root):
            if root in oldToNew:
                return oldToNew[root]

            copy = Node(root.val)
            oldToNew[root] = copy
            for n in root.neighbors:
                copy.neighbors.append(dfs(n))

            return copy

        dfs(node)

        return oldToNew[node]
        