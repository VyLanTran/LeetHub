class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        '''
        4, 7
        
        1, 4
        2, 5
        3, 5
        
        3, 8
        5, 6
        6, 5
        '''
        
        if a == e:
            if c == e and ((b <= d and d <= f) or (f <= d and d <= b)):
                return 2
            return 1
        if b == f:
            # print("here")
            if d == f and ((a <= c and c <= e) or (e <= c and c <= a)):
                return 2
            return 1
        if c - d == e - f:
            if a - b == c - d and ((c <= a and a <= e) or (e <= a and a <= c)):
                return 2
            return 1
        if c + d == e + f:
            if a + b == c + d and ((c <= a and a <= e) or (e <= a and a <= c)):
                return 2
            return 1
        return 2
                
        
        # if a == e or b == f or c - d == e - f or c + d == e + f:
        #     return 1
        # return 2
    
    
    