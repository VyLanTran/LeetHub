class Solution:
    def minMaxDifference(self, num: int) -> int:
        def find_min(num):
            digits = list(str(num))
            goal = digits[0]
            for i, char in enumerate(digits):
                if char == goal:
                    digits[i] = '0'
            return int("".join(digits))

        def find_max(num):
            digits = list(str(num))
            goal = ''
            for i, char in enumerate(digits):
                if goal == '':
                    if char != '9':
                        goal = char
                        digits[i] = '9'
                else:
                    if char == goal:
                        digits[i] = '9'
            return int("".join(digits))
        
        return find_max(num) - find_min(num)


    