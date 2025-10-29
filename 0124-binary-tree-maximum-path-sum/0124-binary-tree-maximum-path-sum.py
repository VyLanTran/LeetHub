# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_global = float('-inf')

        def f(node):
            if not node:
                return 0
            nonlocal max_global
            left_sum, right_sum = f(node.left), f(node.right)
            res = node.val + max(0, left_sum, right_sum)
            max_global = max(max_global, res, node.val + left_sum + right_sum)
            return res

        f(root)
        return max_global