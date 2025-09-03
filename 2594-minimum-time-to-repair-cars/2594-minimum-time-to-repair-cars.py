class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        '''
        time = max(ranks[i] * nums[i])

        where sum(nums[i]) = cars
        find min time

        mechanic with higher rank (smaller number) will repair >= number
        of cars of lower rank mechanics

        6 = 

        r1 n^2 >= r1 (n-1)^2 + r2
        r1 (2n+1) >= r2 (possible)

        binary search on value?

        can a distribution lead to total time <= target?

        5, 1, 8
        cars = 6
        time = 14
        is it possible?
        ie, the mechanics using max time has to be <= 14
        rank: 1, 5, 8
        rem_time = 14 
        num_cars = sqrt(rem_time / r) -> take the floor
        rem_cars -= num_cars
        if every one <= 14 ==> okay

        sqrt(14/1) = 3 cars
        sqrt(14/5) = 1 cars
        sqrt(14/8) = 1 cars
        '''

        # optional
        ranks.sort()

        def is_possible(target):
            cars_done = 0
            for rank in ranks:
                cars_done += int(sqrt(target / rank))
                if cars_done >= cars:
                    return True
            return False

        low, high = 1, ranks[-1] * (cars ** 2)
        best_time = high

        while low <= high:
            mid = low + (high - low) // 2
            if is_possible(mid):
                best_time = mid
                high = mid - 1
            else:
                low = mid + 1

        return best_time



