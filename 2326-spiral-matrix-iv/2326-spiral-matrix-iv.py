# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        curNode = head
        left, right, top, bottom = 0, n - 1, 0, m - 1
        
        breakLoop = False
        
        while left <= right and top <= bottom and curNode:
            # fill top row
            for i in range(left, right + 1):
                if not curNode:
                    breakLoop = True
                    break
                matrix[top][i] = curNode.val
                curNode = curNode.next
            top += 1
            
            # fill right col
            if not curNode or breakLoop:
                break
            for i in range(top, bottom + 1):
                if not curNode:
                    breakLoop = True
                    break
                matrix[i][right] = curNode.val
                curNode = curNode.next
            right -= 1
            
            # fill bottom row
            if not (left <= right and top <= bottom and curNode and not breakLoop):
                break
            for i in range(right, left - 1, -1):
                if not curNode:
                    breakLoop = True
                    break
                matrix[bottom][i] = curNode.val
                curNode = curNode.next
            bottom -= 1
            
            # fill left col
            if not curNode or breakLoop:
                break
            for i in range(bottom, top - 1, -1):
                if not curNode:
                    breakLoop = True
                    break
                matrix[i][left] = curNode.val
                curNode = curNode.next
            left += 1
        
        return matrix
        
        