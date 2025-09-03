class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        '''
        n = number of mechanics
        M = (largest rank) * cars^2

        Time: 
            O(nlog(M) + nlog(n)) if sorting ranks 
            O(nlog(M)) if not sorted
            However, this is in big-O perspective
            In real world, we don't know which is faster
                - sorting first: is_possible() is more likely
                    to terminate early -> better time
                - not sorting: don't have O(nlog(n)) from sorting
                    but in the worst case, if ranks is in descending order,
                    is_possible() may not terminate early, especially if 
                    target time is narrow down (smaller)

        Space: O(1)
        '''

        # optional
        # ranks.sort()

        # O(n)
        def is_possible(target):
            cars_done = 0
            for rank in ranks:
                cars_done += int(sqrt(target / rank))
                if cars_done >= cars:
                    return True
            return False

        # low, high = 1, ranks[-1] * (cars ** 2) # if ranks was sorted
        low, high = 1, max(ranks) * (cars ** 2)
        best_time = high

        while low <= high:
            mid = low + (high - low) // 2
            if is_possible(mid):
                best_time = mid
                high = mid - 1
            else:
                low = mid + 1

        return best_time



