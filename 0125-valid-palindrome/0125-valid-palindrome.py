class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        - len == 1 => True
        - #@#@ => True
        '''

        i, j = 0, len(s) - 1

        while i < j:
            leftChar, rightChar = s[i], s[j]
            if not leftChar.isalnum():
                i += 1
            elif not rightChar.isalnum():
                j -= 1
            elif leftChar.lower() != rightChar.lower():
                return False
            else:
                i += 1
                j -= 1

        return True
        

