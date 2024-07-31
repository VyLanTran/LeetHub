class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        2
        4
        16
        37
        52
        29
        85  64 + 25
        89  64 + 81
        145 25 16 1
        42
        20
        4
        '''
        def sumSqrtDigits(n):
            res = 0
            while n > 0:
                res += pow(n%10, 2)
                n = n // 10
            return res
            
        seenNums = set()
        while True:
            n = sumSqrtDigits(n)
            if n == 1:
                return True
            if n in seenNums:
                return False
            seenNums.add(n)
    
            