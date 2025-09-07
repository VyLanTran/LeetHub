# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def rec(root):
            if not root:
                return True, 0
            is_left_balance, left_depth = rec(root.left)
            if not is_left_balance:
                return False, 0
            is_right_balance, right_depth = rec(root.right)
            if not is_right_balance or abs(left_depth - right_depth) > 1:
                return False, 0
            return True, 1 + max(left_depth, right_depth)

        return rec(root)[0]