class Solution:
    '''
    ab"
    01234567
    eidboaoo
    iiiii
    jjjjjj
    
    a: 0, b: 0
    e: 0
    '''
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0 for _ in range(26)]
        i = 0
        for char in s1:
            index = ord(char) - ord('a')
            freq[index] += 1
        for j in range(len(s2)):
            index = ord(s2[j]) - ord('a')
            freq[index] -= 1
            while freq[index] < 0:
                freq[ord(s2[i]) - ord('a')] += 1
                i += 1
            if j - i + 1 == len(s1):
                return True
        return False
                