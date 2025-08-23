# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
                1
            2       3
        4     5.  6
          7
        return [1, 3, 6, 7]

        [ 6, 5, 4]

        pop all nodes from level 1: 1
        for each node we pop, add its children - right child before left child

        level 2
            node 3 -> add 3 to answer
                add 6
            node 2 (since this is not the first node of this level, don't add to answer)
                add 5, 4

        '''

        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level_size = len(queue)
            res.append(queue[0].val)

            for _ in range(level_size):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return res