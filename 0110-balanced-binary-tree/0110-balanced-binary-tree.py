# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
    
        def helper(root):
            if root is None:
                return (True, 0)
            leftRes = helper(root.left)
            if not leftRes[0]:
                return (False, 0)
            rightRes = helper(root.right)
            if not rightRes[0] or abs(leftRes[1] - rightRes[1]) > 1:
                return (False, 0)
            return (True, 1 + max(leftRes[1], rightRes[1]))
        
        return helper(root)[0]