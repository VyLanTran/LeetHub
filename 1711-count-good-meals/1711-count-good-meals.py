class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        '''
        max sum = sum of 2 largest num
        min sum = sum of 2 smallest num
        what are all powers of 2 in the range
            int(log(min_sum)) <= power <= int(log(max_sum))
            -> list out all 2 ** power

        res = 0, 1, 2, 3, 4
        range: 1 -> 5
        sums = [2, 4, 8, 16, 32]
        (3, 1)
        (5, 3)
        (7, 1)
        (9, 7)
        {
            1: 1
            3: 1
            5: 1
            7: 1
            9: 1
        }
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