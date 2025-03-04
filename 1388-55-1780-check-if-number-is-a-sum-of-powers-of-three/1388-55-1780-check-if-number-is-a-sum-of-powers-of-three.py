class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        '''
        1, 3, 9, 27, 81

        3 + 3 + 3 + 1 10

        3, 9, 9
        '''

        MAX_POWER = int(log(10**8, 3))

        def findMaxPower(n, high):
            low = 0
            maxPower = 0
            while low <= high:
                mid = low + (high - low) // 2
                if 3 ** mid <= n:
                    maxPower = mid
                    low = mid + 1
                else:
                    high = mid - 1
            return maxPower


        prevPower = -1
        high = MAX_POWER
        while n > 0:
            curPower = findMaxPower(n, high)
            # print(n, curPower, 3 ** curPower)
            if curPower == prevPower:
                return False
            prevPower = curPower
            high = curPower
            n -= 3 ** curPower

        return True

    