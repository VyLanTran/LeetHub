# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        
        def rec(node, maxVal):
            if not node:
                return
            nonlocal res
            if node.val >= maxVal:
                res += 1
            rec(node.left, max(maxVal, node.val))
            rec(node.right, max(maxVal, node.val))
            
        rec(root, -inf)
        return res
            