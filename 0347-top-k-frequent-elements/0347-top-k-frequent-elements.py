class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Time: O(nlog(k))
        Space: O(n)
        '''

        counter = Counter(nums)
        min_heap = []

        for num, freq in counter.items():
            if len(min_heap) < k:
                heappush(min_heap, (freq, num))
            elif freq > min_heap[0][0]:
                heappop(min_heap)
                heappush(min_heap, (freq, num))

        return [num for freq, num in min_heap]