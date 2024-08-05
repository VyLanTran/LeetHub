class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        '''
        1, 2, 3, 4
         , 1, 2, 3
         6 5  4
           7. 8. 9
         1211 10
           13 14 15
       1 2 3    
       1 2 3
       4 5 6
       7 8 9
       10 11 12
       
       i / 3 or i / 3 - 1
       row = 1 ==> 1 * 3 + 1 to 2 * 3
            2 ==> 2 * 3 + 1 to 3 * 3
            
            rem = 0 + 3
            
        k = n - 1 = 2
        row = 2 / k or 2 / k - 1 = 0 => left to right
        rem = 2 % k or 2 % k + k = 2
        1 2 3
        
        left to right ==> 1 + rem
        right to left ==> n - rem
        
        '''
        
        k = n - 1
        row = time // k if time % k != 0 else time // k - 1
        rem = time % k if time % k != 0 else k
        return 1 + rem if row % 2 == 0 else n - rem