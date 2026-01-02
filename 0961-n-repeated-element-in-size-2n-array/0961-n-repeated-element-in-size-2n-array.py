class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        '''
        6 = 2 * 3
        '''

        n = len(nums) // 2
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
            if count[num] == n:
                return num