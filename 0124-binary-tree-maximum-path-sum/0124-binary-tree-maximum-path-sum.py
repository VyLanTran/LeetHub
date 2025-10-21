# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        res = 

        f(node) = max sum of a path passing through node but not branch
            if node is None:
                return 0
            left = f(node.left)
            right = f(node.right)
            not_branch_sum = node.val + max(0, left, right)
            res = max(res, not_branch_sum, node.val + left + right)
            return not_branch_sum
        '''

        res = float('-inf')

        def f(node):
            if not node:
                return 0
            nonlocal res
            left_sum = f(node.left)
            right_sum = f(node.right)
            not_branch_sum = node.val + max(0, left_sum, right_sum)
            res = max(res, not_branch_sum, node.val + left_sum + right_sum)
            return not_branch_sum

        f(root)
        return res