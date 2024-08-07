# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # print("a" + 'b')
        allPaths = []
        
        def dfs(root, path):
            if not root:
                return
            if not root.left and not root.right:
                allPaths.append(chr(ord('a') + root.val) + path)
                return
            dfs(root.left, chr(ord('a') + root.val) + path)
            dfs(root.right, chr(ord('a') + root.val) + path)
        
        dfs(root, "")
        return min(allPaths)
            
        
            