# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        '''
        0, 1, 2, 3, 4, 5
        1, 2, 3, 4, 5, 6
        i  i  i  i  i  i  i
        p        p
        c  c  c  c  c  c  c
       
        
        [0]
        
        [1]
        '''
        
        def reverse(head):
            '''
       <-  1  2
            a  b    c        
        while b.next:
        b.next = a
        a = b
        b = c
        c = b.next
        
        ====
        b.next = a
            '''
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
                # print("slowIndex:", slowIndex, "fastIndex:", fastIndex)
                if slowIndex is not None:
                    heads.append(slow)
                    # if slowIndex == 0:
                    #     print("arr should have pointer 1:", heads)
                slowIndex = fastIndex
                slow = fast
                fast = fast.next
                
                # if fastIndex == 0:
                #     print("slow pt should be 1:", slow)
            elif fastIndex % k == k - 1:
                temp = fast.next
                fast.next = None
                fast = temp
            else:
                fast = fast.next
                
            fastIndex += 1
            
        # print("fastIndex:", fastIndex, "slow:", slow)
        if fastIndex % k == 0:
            heads.append(slow)
            
        '''
        [1, 3]
        '''
        
        # print("heads", heads)
        # print("extra:", extraHead)
        
        dummy = ListNode(0)
        cur = dummy
        for node in heads:
            h, t = reverse(node)
            cur.next = h
            cur = t
        cur.next = temp
        
        return dummy.next
        
        
            
        
            
        
        