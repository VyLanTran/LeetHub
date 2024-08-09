# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            curLevel = 1 + max(left, right)
            if curLevel >= len(res):
                res.append([])
            res[curLevel].append(root.val)
            return curLevel
        
        dfs(root)
        
        return res