# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(head):
            if not head or not head.next:
                return head
            a, b, c = None, head, head.next
            
            while b and b.next:
                b.next = a
                a = b
                b = c
                c = b.next
                
            b.next = a
            return b, head
        
        if k == 1:
            return head
        
        slowIndex, fastIndex = None, 0
        slow, fast = None, head
        heads = []
        extraHead = None
        temp = None
        
        while fast:
            if fastIndex % k == 0:
                if slowIndex is not None:
                    heads.append(slow)
                slowIndex = fastIndex
                slow = fast
                fast = fast.next
            elif fastIndex % k == k - 1:
                temp = fast.next
                fast.next = None
                fast = temp
            else:
                fast = fast.next
                
            fastIndex += 1
            
        if fastIndex % k == 0:
            heads.append(slow)
        
        dummy = ListNode(0)
        cur = dummy
        for node in heads:
            h, t = reverse(node)
            cur.next = h
            cur = t
        cur.next = temp
        
        return dummy.next
        
        
            
        
            
        
        