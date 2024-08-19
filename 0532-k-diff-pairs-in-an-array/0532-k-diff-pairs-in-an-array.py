class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        '''
        1, 1, 3, 4, 5
        '''
        
        
        if k > 0:
            uniqueNums = set(nums)
            res = 0
            for num in uniqueNums:
                if num + k in uniqueNums:
                    res += 1
            return res
        
        else:
            freq = dict()
            res = 0
            for num in nums:
                freq[num] = freq.get(num, 0) + 1
            for val in freq.values():
                res += 1 if val > 1 else 0
            return res