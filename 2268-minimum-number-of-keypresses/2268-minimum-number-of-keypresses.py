class Solution:
    def minimumKeypresses(self, s: str) -> int:
        '''
        a: 1
        
        max heap
        
        firstCharNum = 9
        secCharNum = 9
        
        freq: 2, 1, 1, 1
        1 * 12
        '''
        
        freq = dict()
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        arr = [val for val in freq.values()]
        arr.sort(reverse = True)
        
        res = 0
        for i in range(len(arr)):
            if i < 9:
                res += arr[i]
            elif i < 18:
                res += 2 * arr[i]
            else:
                res += 3 * arr[i]
        return res
        