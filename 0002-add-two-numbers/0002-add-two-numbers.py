# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        m = number of digits of l1
        n = number of digits of fl2

        Time: O(max(m, n))
        Space: O(1) - no auxiliary space
        '''
        carry = 0
        dummy = ListNode(-1)
        cur = dummy

        while l1 or l2:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            cur.next = ListNode((digit1 + digit2 + carry) % 10)
            carry = (digit1 + digit2 + carry) // 10
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            cur.next = ListNode(carry)

        return dummy.next