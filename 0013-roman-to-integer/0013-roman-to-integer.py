class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        MCMXCIV
        1000(M) + 900 (CM) + 90(XC) + 4(IV)

        '''

        symbol_to_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0
        n = len(s)
        i = 0

        while i < n:
            char = s[i]
            if i + 1 < n:
                next_char = s[i + 1]
                if symbol_to_val[char] < symbol_to_val[next_char]:
                    res += symbol_to_val[next_char] - symbol_to_val[char]
                    i += 2
                    continue
            res += symbol_to_val[char]
            i += 1

        return res

