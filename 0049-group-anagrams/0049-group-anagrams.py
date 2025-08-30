class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        n = number of strings
        m = max len of a string

        Time: O(mn)
        Space: O(n)
        '''

        def encode(s):
            letter_freq = [0 for _ in range(26)]
            for char in s:
                letter_freq[ord(char) - ord('a')] += 1
            return tuple(letter_freq)

        anagram_map = defaultdict(list)

        for s in strs:
            anagram_map[encode(s)].append(s)

        return list(anagram_map.values())