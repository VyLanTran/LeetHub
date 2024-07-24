class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            if len(minHeap) < k:
                heappush(minHeap, num)
            elif minHeap[0] > num:
                continue
            else:
                heappop(minHeap)
                heappush(minHeap, num)
                
        return minHeap[0]