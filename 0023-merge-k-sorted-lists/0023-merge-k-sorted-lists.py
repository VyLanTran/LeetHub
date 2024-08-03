# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        pointer = 0
        minHeap = []
        for head in lists:
            if head:
                heappush(minHeap, (head.val, pointer, head))
                pointer += 1
        while minHeap:
            node = heappop(minHeap)[2]
            cur.next = node
            cur = cur.next
            if node.next:
                heappush(minHeap, (node.next.val, pointer, node.next))
                pointer += 1
        return dummy.next
                