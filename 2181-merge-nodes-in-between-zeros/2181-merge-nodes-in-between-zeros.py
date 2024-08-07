# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        0, 3, 1, 0, 4, 5, 2, 0
           i  i  i  i  i  i  i
        sum = 11
        if node.val == 0 ==> insert current sum then reset then cur = cur.next
        dummy -> 4, 11
        '''
        
        dummy = ListNode(0)
        cur = dummy
        sum, i = 0, head.next
        
        while i:
            if i.val == 0:
                if sum != 0:
                    cur.next = ListNode(sum)
                    cur = cur.next
                sum = 0
            else:
                sum += i.val
            i = i.next
        return dummy.next
            