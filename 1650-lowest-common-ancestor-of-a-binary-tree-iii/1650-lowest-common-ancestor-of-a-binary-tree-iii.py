"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        '''
        n = number of nodes in the tree
        Time: O(n) - in the worse case (tree looks like a linked list)
        Space: O(1)
        '''
        a, b = p, q

        while a != b:
            a = a.parent
            b = b.parent
            if not a:
                a = q
            if not b:
                b = p
        
        return a