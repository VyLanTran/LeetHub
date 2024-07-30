class Solution:
    def partitionLabels(self, s: str) -> List[int]:
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