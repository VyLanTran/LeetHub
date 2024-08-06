# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        def findTail(head):
            cur = head
            while cur:
                if not cur.next:
                    return cur
                cur = cur.next
            return None
        
        cur = list1
        point1, point2, point3 = None, None, None
        i = 0
        while cur:
            if i + 1 == a:
                point1 = cur
            elif i == b:
                point2 = cur
                point3 = cur.next
                break
            else:
                pass
            cur = cur.next
            i += 1
        point2.next = None
        point1.next = list2
        tail2 = findTail(list2)
        tail2.next = point3
        return list1
        
            