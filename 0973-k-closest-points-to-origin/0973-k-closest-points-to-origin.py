class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        n = number of points in array
        Time: O(nlog(k))
        Space: O(k)
        '''

        max_heap = []

        for i, point in enumerate(points):
            x, y = point
            dist_squared = x ** 2 + y ** 2
            if len(max_heap) >= k and dist_squared >= -max_heap[0][0]:
                continue
            if len(max_heap) >= k:
                heappop(max_heap)
            heappush(max_heap, (-dist_squared, i))

        return [points[tup[1]] for tup in max_heap]
        