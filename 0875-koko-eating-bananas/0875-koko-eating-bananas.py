class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        [3, 6, 7, 11]
        
        '''
        
        left, right = 1, max(piles)
        
        def canFinish(k):
            totalTime = 0
            for pile in piles:
                totalTime += ceil(pile / k)
                if totalTime > h:
                    return False
            return True
        
        res = right
        while left <= right:
            mid = left + (right - left) // 2
            if canFinish(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
                