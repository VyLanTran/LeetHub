# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            maxVal = -inf
            for i in range(size):
                front = queue.popleft()
                maxVal = max(maxVal, front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            res.append(maxVal)
        
        return res
        