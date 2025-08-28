# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Time: O(n), n = number of nodes in the tree
        Space: O(n), in the worse case, tree is a string-shape thus the 
        stack size is O(n)
        '''
        # if not root:
        #     return root
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # root.left, root.right = root.right, root.left

        # return root

        '''
        Time: O(n)
        Space: O(n//2) = O(n)
        '''

        if not root:
            return root

        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return root


            