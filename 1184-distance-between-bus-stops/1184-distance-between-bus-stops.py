class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        '''
        0,1,2,3
        1,2,3,4

        clockwise_dist between i < j is sum(distance[k]) for i <= k < j
        counter = total - clockwise_dist

        0, 1,2, 3, 4, 5,6,7
        7,10,1,12,11,14,5,0
        '''

        total_dist, clockwise_dist = 0, 0
        start, destination = min(start, destination), max(start, destination)

        for i, dist in enumerate(distance):
            if start <= i < destination:
                clockwise_dist += dist
            total_dist += dist

        return min(clockwise_dist, total_dist - clockwise_dist)