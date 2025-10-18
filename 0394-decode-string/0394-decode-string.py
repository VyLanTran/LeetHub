class Solution:
    def decodeString(self, s: str) -> str:
        '''
        3[a]2[bc]
        iiii
        stack = 

        string = a
        freq - 
        '''

        n = len(s)
        stack = []
        i = 0

        while i < n:
            char = s[i]
            if char.isnumeric():
                j = i
                while j < n and s[j].isnumeric():
                    j += 1
                stack.append(s[i:j])
                i = j
            elif char.isalpha():
                j = i
                while j < n and s[j].isalpha():
                    j += 1
                string = s[i:j]
                if stack and stack[-1].isalpha():
                    prev_string = stack.pop()
                    string = prev_string + string
                stack.append(string)
                i = j
            elif char == ']':
                string = stack.pop()
                freq = int(stack.pop())
                string = string * freq
                if stack and stack[-1].isalpha():
                    prev_string = stack.pop()
                    string = prev_string + string
                stack.append(string)
                i += 1
            else:
                i += 1

        return stack[0]

