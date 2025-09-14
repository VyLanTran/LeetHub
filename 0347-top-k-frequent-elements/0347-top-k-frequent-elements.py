class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        max_heap = [(-val, key) for key, val in counter.items()]
        heapq.heapify(max_heap)
        res = []

        for _ in range(k):
            neg_count, key = heapq.heappop(max_heap)
            res.append(key)

        return res
