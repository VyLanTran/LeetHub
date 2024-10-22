# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque()
        minHeap = []
        queue.append(root)
        
        while queue:
            size = len(queue)
            total = 0
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(minHeap) < k:
                heappush(minHeap, total)
            elif total > minHeap[0]:
                heappop(minHeap)
                heappush(minHeap, total)
            else:
                pass
            
        return minHeap[0] if len(minHeap) >= k else -1