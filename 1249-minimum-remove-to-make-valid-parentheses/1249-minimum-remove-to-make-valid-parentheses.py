class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        '''
        res = list(s)
        if letter, we don't care, just skip
            
        if (, add to arr
        if see ):
            if stack has open paren:
                pop
            else:
                delete this ), one more deletion use
                how? replace with ''

        at the end, what if still has open paren?
        record their index
        replace with ''
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