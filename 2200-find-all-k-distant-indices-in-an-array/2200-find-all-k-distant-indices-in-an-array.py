class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        '''
        0,1,2,3,4,5,6
        3,4,9,1,3,9,5
        i i i i

        [2, 5] -> [1, 2, 3, 4, 5, 6]
        [3, 4] -> [] 

        [i-1,(i),i+1]

        if nums[i] == target:
            if res and nums[i] == res[-1]:
                add i + 1 if i + 1 < n
            else:
                if i - 1 >= 0:
                    add i-1
                if i + 1 < n:
                    add i + 1
                add i

        [3, 6], k = 2
        [1, 5], [4, 8]

        prev_right = -1
        num = 3
            left = 1 + max(prev_right, num - k) = 1
            right = min(n-1, num + k) = 5
            prev_right = right
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