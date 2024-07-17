# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        found = 0
        
        def rec(root, p, q):
            nonlocal found
            if found >= 2 or not root:
                return None
            if root.val == p.val or root.val == q.val:
                found += 1
                return root
            left = rec(root.left, p, q)
            right = rec(root.right, p, q)
            if not left:
                return right
            return root if right else left
        
        return rec(root, p, q)
            