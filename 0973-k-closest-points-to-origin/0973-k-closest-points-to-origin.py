class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        def calSquDist(point):
            return pow(point[0], 2) + pow(point[1], 2)
        
        for point in points:
            if len(maxHeap) < k:
                heappush(maxHeap, (-calSquDist(point), point))
                continue
            dist = calSquDist(point)
            if dist >= -maxHeap[0][0]:
                continue
            heappop(maxHeap)
            heappush(maxHeap, (-dist, point))
            
        res = []
        while maxHeap:
            res.append(heappop(maxHeap)[1])
        return res
            