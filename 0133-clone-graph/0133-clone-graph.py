"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        new_map={}
        new_map[node]= Node(node.val)

        queue=[node]

        while queue:
            current=queue.pop(0)

            for neighbor in current.neighbors:
                if neighbor not in new_map:
                    new_map[neighbor]=Node(neighbor.val)
                    queue.append(neighbor)

                new_map[current].neighbors.append(new_map[neighbor])

        return new_map[node]



        