class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        - no alphanumeric -> True

        left, right
        while left <= right:
            if left char is not alphanumeric:
                left += 1
            elif right char is not alphanumeric:
                right -= 1
            else:
                convert both into lowercase
                if not match:
                    return False
                left += 1
                right -= 1
        '''

        left, right = 0, len(s) - 1

        while left <= right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        
        return True
