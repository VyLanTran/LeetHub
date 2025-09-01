class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Time: O(nlog(k))
        Space: O(k)
        '''

        min_heap = [nums[i] for i in range(k)]
        heapify(min_heap)

        for i in range(k, len(nums)):
            num = nums[i]
            if num > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, num)

        return min_heap[0]