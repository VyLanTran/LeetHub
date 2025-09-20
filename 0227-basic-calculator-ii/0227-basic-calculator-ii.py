class Solution:
    def calculate(self, s: str) -> int:
        '''

        if char is number:
            val = ""
            traverse until hit a non-numeric val
            val -> int
            put into stack
       

        sum all the value in stack

        '''

        i = 0
        stack = []
        
        while i < len(s):
            char = s[i]
            if char == ' ':
                i += 1
            elif char in "+-*/":
                i += 1
                op2 = ""
                while i < len(s) and s[i] == ' ':
                    i += 1
                while i < len(s) and s[i].isnumeric():
                    op2 += s[i]
                    i += 1
                op2 = int(op2)

                if char == '*':
                    op1 = stack.pop()
                    stack.append(op1 * op2)
                elif char == '/':
                    op1 = stack.pop()
                    stack.append(int(op1 / op2))
                elif char == '+':
                    stack.append(op2)
                else:
                    stack.append(-op2)
            else:
                op2 = ""
                while i < len(s) and s[i].isnumeric():
                    op2 += s[i]
                    i += 1
                stack.append(int(op2))
            
        return sum(stack)