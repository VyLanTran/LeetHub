class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        
        '''
        24 15 = 8, 5
        
        gcd(24, 15)
        gcd(15, 24%15=9)
        gcd(9, 15%9=6)
        gcd(6, 9%6=3)
        gcd(3, 0) = 3
        
        
        '''
        
        def fracAdd(num1, denom1, num2, denom2):
            return num1*denom2+num2*denom1, denom1*denom2
        
        
        
        def fracReduce(num, denom):
            commonFactor = gcd(num, denom)
            return num//commonFactor, denom//commonFactor
        
        curNum, curDenom = 0, 1
        isPos = False
        if expression[0] != "-":
            expression = "+" + expression
            isPos = True
        
        i = 0
        while i < len(expression):
            c = expression[i]
            if c != "-" and c != "+":
                break
            isPos = c == "+"
            i += 1
            num, denom = "", ""
            while i < len(expression) and expression[i] != "/":
                num += expression[i]
                i += 1
            i += 1
            while i < len(expression) and expression[i].isdigit():
                denom += expression[i]
                i += 1
            num, denom = int(num), int(denom)
            num *= 1 if isPos else -1
            curNum, curDenom = fracAdd(curNum, curDenom, num, denom)
            
        curNum, curDenom = fracReduce(curNum, curDenom)
        return str(curNum) + "/" + str(curDenom)
        
            
        
            