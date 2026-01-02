# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        2 -> 1 ->  3  <- 4
                   a    b   c
        3 -> 
        dummy = 2
        '''
        if not head or not head.next:
            return head
        a, b, c = head, head.next, head.next.next
        dummy = ListNode(-1)
        cur = dummy

        while True:
            a.next = c
            b.next = a
            cur.next = b
            cur = a
            a = c
            if not a or not a.next:
                break
            b = a.next
            c = b.next
        return dummy.next 
     