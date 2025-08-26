class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        '''
        Time: O(1)
        '''

        return min(maxWeight // w, n * n)