class Solution:
    def calculate(self, s: str) -> int:
        last_val, last_operator = None, None
        i = 0
        res = 0

        while i < len(s):
            char = s[i]
            if char == ' ':
                i += 1
            elif char in "+-*/":
                last_operator = char
                i += 1
            else:
                cur_val = ""
                while i < len(s) and s[i].isnumeric():
                    cur_val += s[i]
                    i += 1
                cur_val = int(cur_val)
                if not last_operator:
                    last_val = cur_val
                    continue
                elif last_operator in "+-":
                    res += last_val
                    last_val = cur_val if last_operator == '+' else -cur_val
                elif last_operator == '*':
                    last_val *= cur_val
                elif last_operator == '/':
                    last_val = int(last_val / cur_val)
        res += last_val 

        return res

        