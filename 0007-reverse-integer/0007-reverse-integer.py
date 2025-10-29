class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        UPPER = 2**31

        while x > 0:
            digit = x % 10
            if res > (UPPER - digit)/10:
                return 0
            res = res * 10 + digit
            x //= 10
        
        return res * sign