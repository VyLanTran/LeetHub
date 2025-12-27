class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        12
        12

        1
        12
        '''

        if x < 0:
            return False
        if x % 10 == 0:
            return x == 0
        rev = 0
        while rev < x:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
            if rev == x:
                return True
            if rev > x and rev // 10 == x:
                return True
        return False