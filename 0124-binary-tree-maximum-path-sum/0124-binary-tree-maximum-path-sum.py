# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = float('-inf')

        def rec(node):
            if not node:
                return 0
            nonlocal res
            left_sum = rec(node.left)
            right_sum = rec(node.right)
            res = max(res, node.val + max(0, left_sum) + max(0, right_sum))
            return node.val + max(0, left_sum, right_sum)

        rec(root)
        return res