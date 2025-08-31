class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        '''
        Time: O(n)
        Space: O(n)
        '''
        counter = Counter(nums)

        for val in counter.values():
            if val > 2:
                return False
        
        return True