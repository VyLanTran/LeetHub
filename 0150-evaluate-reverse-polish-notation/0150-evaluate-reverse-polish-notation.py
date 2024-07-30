class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for token in tokens:
            if token in "+-*/":
                num2, num1 = arr.pop(), arr.pop()
                if token == "+":
                    arr.append(int(num1 + num2))
                elif token == "-":
                    arr.append(int(num1 - num2))
                elif token == "*":
                    arr.append(int(num1 * num2))
                else:
                    arr.append(int(num1 / num2))
            else:
                arr.append(int(token))
        return arr[0]
        
