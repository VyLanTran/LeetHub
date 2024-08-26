"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        def rec(node):
            if not node:
                return
            for child in node.children:
                rec(child)
            res.append(node.val)
        
        rec(root)
        return res
            