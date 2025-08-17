class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        a: 3
        n: 1
        g: 1
        r: 1
        m: 1

        - if not same length --> false
        - find letter frequency for s
        - loop through t
            - if freq in s = 0 --> False
            - else, -1
        

        test cases:
        1. not same length -> F

        Time: O(m + n), m = len(s), n = len(t)
        Space: O(1)
        '''

        if len(s) != len(t):
            return False
        letter_freq = [0 for _ in range(26)]

        for letter in s:
            letter_freq[ord(letter) - ord('a')] += 1

        for letter in t:
            index = ord(letter) - ord('a')
            if letter_freq[index] == 0:
                return False
            letter_freq[index] -= 1

        return True
