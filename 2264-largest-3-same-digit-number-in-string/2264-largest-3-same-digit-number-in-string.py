class Solution:
    def largestGoodInteger(self, num: str) -> str:
        '''
        Time: O(n)
        Space: O(1)
        '''
        max_digit = -1
        i = 0

        while i < len(num):
            j = i
            while j < len(num) and num[j] == num[i]:
                j += 1
            if j - i >= 3:
                max_digit = max(max_digit, int(num[i]))
            i = j

        return "" if max_digit == -1 else str(max_digit) * 3