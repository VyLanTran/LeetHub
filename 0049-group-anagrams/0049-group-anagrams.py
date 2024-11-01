class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def countFrequency(word):
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            return tuple(freq)
        
        anagrams = defaultdict(list)
        for word in strs:
            pattern = countFrequency(word)
            anagrams[pattern].append(word)
        res = []
        for arr in anagrams.values():
            res.append(arr)
        return res