class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        '''
        Time: O(n)
        '''
        # return sum([i for i in range(1, n + 1) if i % m != 0]) - sum([i for i in range(1, n + 1) if i % m == 0])

        sum_n = n * (n + 1) // 2
        start, end = m, n // m * m
        count = (end - start) // m + 1
        sum_divisible = (start + end) * count // 2
        return sum_n - sum_divisible * 2