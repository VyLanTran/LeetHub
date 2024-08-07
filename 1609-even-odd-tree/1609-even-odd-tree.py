# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2 == 0:
            return False
        
        queue = deque()
        level = 0
        queue.append(root)
        
        while queue:
            size = len(queue)
            cur = float('inf') if level % 2 == 1 else float('-inf')
            for i in range(size):
                node = queue.popleft()
                num = node.val
                if (num - level) % 2 == 0:
                    return False
                if level % 2 == 0 and num <= cur:
                    return False
                if level % 2 == 1 and num >= cur:
                    return False
                cur = num
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
            
        return True
                