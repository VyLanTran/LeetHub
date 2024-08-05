class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        '''
        01234567
        aabcbbca
        
        a:3, [0,1,7]
        b:3  [2,4,5]
        c:2  [3,6]
        
        0123
        abcd
        
        
        '''
        
        map = dict()
        for i in range(len(s)):
            c = s[i]
            if c not in map:
                map[c] = (0, [])
            (freq, arr) = map[c]
            arr.append(i)
            map[c] = (freq + 1, arr)
        maxHeap = [(-map[c][0], map[c][1][-1], c) for c in map]
        heapify(maxHeap)
        maxFreq = maxHeap[0][0]
        res = ""
        while maxHeap and maxHeap[0][0] == maxFreq:
            res += heappop(maxHeap)[-1]

        return res
                