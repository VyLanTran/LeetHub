class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        numDrink, numFull, numEmpty = 0, numBottles, 0
        
        while numFull > 0:
            numEmpty += numFull
            numDrink += numFull
            numFull = numEmpty // numExchange
            numEmpty %= numExchange
            
        
        return numDrink