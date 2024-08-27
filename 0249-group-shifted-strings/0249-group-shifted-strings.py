class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # print(ord('a') + 26, ord('b'))
        # print(ord('z') + 1 - 26)
        def formatStr(s):
            steps = ord(s[0]) - ord('a')
            res = ""
            for c in s:
                val = ord(c)
                val -= steps
                if val < ord('a'):
                    val += 26
                res += chr(val)
            return res
        
        map = defaultdict(list)
        for s in strings: 
            formatted = formatStr(s)
            map[formatted].append(s)
            
        res = map.values()
        
        return res
        
        # print(ord('a') - 1 + 26, ord('z'))
        # print(formatStr("abc"))
        
            