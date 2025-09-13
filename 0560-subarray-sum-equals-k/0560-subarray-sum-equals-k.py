class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        cur_sum = 0
        res = 0

        for num in nums:
            cur_sum += num
            res += prefix_sums[cur_sum - k]
            prefix_sums[cur_sum] += 1

        return res

