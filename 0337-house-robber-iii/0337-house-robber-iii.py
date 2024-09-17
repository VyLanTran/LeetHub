# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        '''
        f(node)
        if skip: f(node.left) + f(node.right)
        if rob:  val + f(node.left.left) + f.(node.left.right) + f(node.right.left) + f(node.right.right)
        if node is None ==> 0
        
        f(3root)
            3 + f(null) + f(3leaf) + f(null) + f(1)
            
        '''
        if not root:
            return 0
        
#         def levelTraversal():
#             allNodes = []
#             queue = deque(root)
#             while queue:
#                 n = len(queue)
#                 for _ in range(n):
#                     front = queue.popleft()
#                     allNodes.append(front)
#                     if front.left:
#                         queue.append(front.left)
#                     if front.right:
#                         queue.append(front.right)
#             return allNodes
        
#         allNodes = levelTraversal()
#         dp
            
        dp = {}
        
        def rec(node):
            if not node:
                return 0
            if node in dp:
                return dp[node]
            
            robValue = node.val + (rec(node.left.left) if node.left else 0) + (rec(node.left.right) if node.left else 0) + (rec(node.right.left) if node.right else 0) + (rec(node.right.right) if node.right else 0)
            
            skipValue = rec(node.left) + rec(node.right)
            dp[node] = max(robValue, skipValue)
            return dp[node]
        
        return rec(root)
            