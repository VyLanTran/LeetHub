class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Time: O(nlog(n)) - for heapify and heappush
        Space: O(1)
        '''
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            y, x = heappop(stones), heappop(stones)
            x = -x
            y = -y
            if y > x:
                heappush(stones, -(y - x))

        return -stones[0] if len(stones) == 1 else 0
