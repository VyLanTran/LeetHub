class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # counter = Counter(nums)
        # for key, val in counter.items():
        #     if val > len(nums) // 2:
        #         return key

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate