# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        first rturn a list containing all max depth nodes
        res = [7, 4, 9]

        f(3)
            l = f(5) = 2
                l = f(6) = None
                    l = r = None
                r = f(2) = 2
                    l = f(7) = 7
                        7 itself is in list, so just return itself
                    r = f(4) = 4
                    both child is not None, so return parent (me)
                return the non-none child
                    
        '''

        deepest_nodes = set()
        max_depth = -1
        queue = deque([(root, 0)])

        while queue:
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
                deepest_nodes = set([node])
            elif depth == max_depth:
                deepest_nodes.add(node)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        
        def rec(node):
            if not node:
                return None
            if node in deepest_nodes:
                return node
            left = rec(node.left)
            right = rec(node.right)
            if left and right:
                return node
            return left if left else right

        return rec(root)





        
            
            
