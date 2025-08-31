class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        '''
        n = len of array
        k = max value in array
        Time: O(nlog(k)) 
        Space: O(log(k) + n) = O(n) - this is worst case, when all value are distinct
        '''

        MOD = 10 ** 9 + 7
        res = 0
        min_val = min(deliciousness)
        start = int(log(min_val * 2, 2)) if min_val != 0 else 0
        end = int(log(max(deliciousness) * 2, 2)) 
        possible_sums = []
        counter = defaultdict(int)

        for power in range(start, end + 1):
            possible_sums.append(2 ** power)

        for num in deliciousness:
            for goal in possible_sums:
                res += counter[goal - num]
            counter[num] += 1

        return res % MOD