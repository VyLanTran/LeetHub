# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        [1, 2,]

        '''
        stack = []
        index = 0

        cur = head
        while cur != None:
            stack.append((cur.val, index))
            total = 0
            i = len(stack) - 1
            while i >= 0:
                total += stack[i][0]
                if total == 0:
                    # print(f"total = 0, i = {i}, index = {index}")
                    stack = stack[0:i]
                    break
                i -= 1
            cur = cur.next
            index += 1

        print(f"mystack = {stack}")

        i, j = 0, 0
        dummy = ListNode(-1)
        cur = head
        pointer = dummy

        while cur != None:
            if j >= len(stack):
                pointer.next = None
                break
            if i == stack[j][1]:
                pointer.next = cur
                pointer = pointer.next
                j += 1
            cur = cur.next
            i += 1

        return dummy.next




        

            

        