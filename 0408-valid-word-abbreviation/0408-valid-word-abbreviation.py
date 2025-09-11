class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        '''
        m = len(word)
        n = len(abbr)
        Time: O(min(m, n))
        Space: O(n)
        '''

        word_len, abbr_len = len(word), len(abbr)
        i, j = 0, 0

        while i < word_len and j < abbr_len:
            abbr_char = abbr[j]
            if abbr_char.isalpha():
                if abbr_char != word[i]:
                    return False
                i += 1
                j += 1
            elif abbr_char == '0':
                return False
            else:
                num_string = ""
                while j < abbr_len and abbr[j].isnumeric():
                    num_string += abbr[j]
                    j += 1
                i += int(num_string)
        
        return i == word_len and j == abbr_len
