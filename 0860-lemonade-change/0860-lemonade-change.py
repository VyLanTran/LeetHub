class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        5: 0
        10: 0
        20: 0
        
        pay 10 => return 5
        pay 20 => return 15 => always prioritize 10 + 5
        '''
        
        freq = {5:0, 10:0, 20:0}
        for bill in bills:
            if bill == 5:
                pass
            elif bill == 10:
                if freq[5] <= 0:
                    return False
                freq[5] -= 1
            else:
                if freq[10] <= 0:
                    if freq[5] <= 2:
                        return False
                    freq[5] -= 3
                else:
                    if freq[5] <= 0:
                        return False
                    freq[10] -= 1
                    freq[5] -= 1
            freq[bill] += 1
        return True