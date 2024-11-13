class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        a: 1, b: 1
        
        eibbaoo
        rrrrr
        llll
        
        e: 0
        i: 0
        b: 1
        a: 1
        '''
        
        def countFreq(s):
            freq = defaultdict(int)
            for char in s:
                freq[char] += 1
            return freq
        
        freq1 = countFreq(s1)
        freq2 = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            char = s2[right]
            freq2[char] += 1
            while freq2[char] > freq1[char]:
                leftChar = s2[left]
                freq2[leftChar] -= 1
                left += 1
            if right - left + 1 == len(s1):
                return True
            
        return False