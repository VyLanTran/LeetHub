class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        '''
        Time: O(n)
        Space: O(n)
        '''

        target_indices = [i for i, num in enumerate(nums) if num == key]
        prev_right = -1
        res = []

        for i in target_indices:
            left = max(prev_right + 1, i - k)
            right = min(len(nums) - 1, i + k)
            res.extend([j for j in range(left, right + 1)])
            prev_right = right
        
        return res