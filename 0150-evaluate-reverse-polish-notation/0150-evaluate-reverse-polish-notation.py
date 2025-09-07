class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
         i.    i. i.  i.   i.  i.   i.  i.   i

        stack: "0"

        if isnumeric():
            add to stack
        else:
            op2 = pop()
            op1 = pop()
            res = op1 <operand> op2
            push res to stack

        -6 / 4 = -1.5 -> 0
        '''

        res = 0
        stack = []

        def calculate(op1, op2, operator):
            if operator == "+":
                return op1 + op2
            elif operator == "-":
                return op1 - op2
            elif operator == "*":
                return op1 * op2
            return int(op1 / op2)
        
        for token in tokens:
            if token in "+-*/":
                op2 = int(stack.pop())
                op1 = int(stack.pop())
                stack.append(str(calculate(op1, op2, token)))
            else:
                stack.append(token)

        return int(stack[0])

