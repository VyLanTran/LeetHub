# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        '''
        {
            1: 2, 3
            2: 1, 4
            4: 2, 5
            5: 4, 6
            6: 5
            3 :1
        }
        
        dfs(1, parent = None)
            dfs(2, parent = 1)
                dfs(4, 2)
                    dfs(5, 4)
                        dfs(6, 5)
            dfs(3)
                    
            
        
        '''
        
        def buildGraph():
            graph = dict()
            leaves = set()
            
            def dfs(node, parent):
                if not node:
                    return
                if not node.left and not node.right:
                    leaves.add(node.val)
                if node.val not in graph:
                    graph[node.val] = []
                if parent:
                    graph[node.val].append(parent.val)
                if node.left:
                    graph[node.val].append(node.left.val)
                    dfs(node.left, node)
                if node.right:
                    graph[node.val].append(node.right.val)
                    dfs(node.right, node)
            dfs(root, None)
            return graph, leaves
        
        graph, leaves = buildGraph()
        
        if k in leaves:
            return k
        queue = deque()
        queue.append(k)
        visited = set()
        
        while queue:
            size = len(queue)
            for _ in range(size):
                val = queue.popleft()
                if val in graph:
                    for neighbor in graph[val]:
                        if neighbor in visited:
                            continue
                        if neighbor in leaves:
                            return neighbor
                        visited.add(neighbor)
                        queue.append(neighbor)
        return k
        
        
            