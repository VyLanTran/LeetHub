class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_freq = defaultdict(int)

        for num in nums:
            num_freq[num] += 1

        for val in num_freq.values():
            if val % 2 == 1:
                return False

        return True