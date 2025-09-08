# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        '''
        Time: O(n)
        Space: O(n) - actually, O(n/2) since the largest size at a time is when it holds the broadest level (last level when tree is balanced)
        '''

        if not root:
            return []
        queue = deque([root])
        res = []

        while queue:
            size = len(queue)
            level_arr = []
            for _ in range(size):
                node = queue.popleft()
                level_arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_arr)

        return res