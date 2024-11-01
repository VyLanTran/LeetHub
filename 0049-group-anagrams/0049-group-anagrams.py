class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
       
        
        anagrams = defaultdict(list)
        for word in strs:
            pattern = ''.join(sorted(word))
            anagrams[pattern].append(word)
        return list(anagrams.values())