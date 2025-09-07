class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        k = max pile
        Time: O(nlog(k))
        Space: O(1)
        '''

        left, right = 1, max(piles)
        min_speed = right

        def is_possible(speed):
            return sum(ceil(pile / speed) for pile in piles) <= h

        while left <= right:
            mid = left + (right - left) // 2
            if is_possible(mid):
                min_speed = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return min_speed