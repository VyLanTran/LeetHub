# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])
    
#         queue = deque()
#         queue.append(root)
#         isLevelFull, lastNodeNextLevel = True, False
#         level = 0
        
#         while queue:
#             if not isLevelFull:
#                 return False
#             isLevelFull = len(queue) == pow(2, level)
#             for _ in range(len(queue)):
#                 node = queue.popleft()
#                 if lastNodeNextLevel and (node.left or node.right):
#                     return False
#                 if not node.left and node.right:
#                     return False
#                 if not node.left or not node.right:
#                     lastNodeNextLevel = True
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             level += 1
#         return True
            
            