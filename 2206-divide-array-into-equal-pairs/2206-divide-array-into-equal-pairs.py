class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        num_freq = Counter(nums)
        return all(freq % 2 == 0 for freq in num_freq.values())