# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        '''
        f(1)
            l = f(3) = False ==> node.left = None
                l = f(3) = True
                r = f(2) = False
        f(3) = True
        
        '''
        
        def dfs(root):
            if not root:
                return True
            left = dfs(root.left)
            right = dfs(root.right)
            if left:
                root.left = None
            if right:
                root.right = None
            if left and right and root.val == target:
                return True
        
        res = dfs(root)
        return root if not res else None
            