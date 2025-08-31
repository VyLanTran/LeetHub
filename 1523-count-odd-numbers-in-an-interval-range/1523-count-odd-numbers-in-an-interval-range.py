class Solution:
    def countOdds(self, low: int, high: int) -> int:
        '''
        Time: O(1)
        Space: O(1)
        '''
        start = low if low % 2 == 1 else low + 1
        end = high if high % 2 == 1 else high - 1

        return (end - start) // 2 + 1