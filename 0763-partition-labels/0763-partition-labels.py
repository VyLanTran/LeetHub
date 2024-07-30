class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        '''
        012345678901234567890123
        ababcbacadefegdehijhklij
        i        i
        res = 
        a:0, 8
        b:1, 5
        c:4, 7
        d:9, 9
        e:10, 15
        f:11, 11
        g:13, 13
        h:16, 19
        i:17, 22 
        j:18, 23
        k:20, 20
        l:21, 21
        
        0, 8
        9, 9
        10, 15
        16, 23
        '''
        
        map = dict()
        for i in range(len(s)):
            c = s[i]
            if c not in map:
                map[c] = (i, i)
            else:
                map[c] = (map[c][0], i)
        
        
        arr = []
        for tup in map.values():
            arr.append(tup)
        heapify(arr)
        
        res = []
        cur = arr[0]
        for i in range(1, len(arr)):
            next = arr[i]
            if next[0] > cur[1]:
                res.append(cur[1] - cur[0] + 1)
                cur = next
            else:
                cur = (cur[0], max(cur[1], next[1]))
        res.append(cur[1] - cur[0] + 1)
        return res