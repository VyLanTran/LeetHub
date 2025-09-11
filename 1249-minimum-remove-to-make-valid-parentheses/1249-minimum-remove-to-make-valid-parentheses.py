class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        Time: O(n)
        Space: O(n)
        '''

        s = list(s)
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        for i in stack:
            s[i] = ''
        
        return "".join(s)