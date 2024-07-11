class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        res = []
        
        def hash(word):
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            res = ""
            for i in range(26):
                res += chr(ord('a') + i) + str(count[i])
            return res
        
        for word in strs:
            hashedStr = hash(word)
            if not hashedStr in map:
                map[hashedStr] = [word]
            else:
                map[hashedStr].append(word)
        for value in map.values():
            res.append(value)
        
        return res
            