class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            y, x = heappop(stones), heappop(stones)
            if x != y:
                heappush(stones, y - x)
        return 0 if not stones else -stones[0]
        