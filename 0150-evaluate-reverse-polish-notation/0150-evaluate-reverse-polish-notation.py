class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Time: O(n)
        Space: O(n)
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

