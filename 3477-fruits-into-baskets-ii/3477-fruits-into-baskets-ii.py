class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        '''
            0, 1, 2
        f = 4, 2, 5

            0, 1, 2
        b = 3, 5, 4

        available baskets = 3, 5, 2
        '''

        n = len(baskets)
        is_available = [True for _ in range(n)] 
        res = 0

        for fruit in fruits:
            can_place = False
            for i, basket in enumerate(baskets):
                if is_available[i] and fruit <= basket:
                    is_available[i] = False
                    can_place = True
                    break
            if not can_place:
                res += 1

        return res
            
            

