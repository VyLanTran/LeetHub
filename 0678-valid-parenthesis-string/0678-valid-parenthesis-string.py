class Solution:
    def checkValidString(self, s: str) -> bool:
        '''
        f(i, num_closes)
            if i < 0:
                return num_closes == 0
                # but also need to make sure ( always followed by ) in correct order
            char
            if char == ):
                return f(i - 1, num_closes + 1)
            elif char == (:
                if num_closes <= 0:
                    return False
                return f(i - 1, num_closes - 1)
            else:
                res = False
                if num_closes > 0:
                    res = res or f(i - 1, num_closes - 1)
                # if it's a close
                res = res or f(i - 1, num_closes + 1)
                # if it's an empty
                res = res or f(i - 1, num_closes)

        0123
        (*))

        f(3, 0)
            f(2, 1)
                f(1, 2)
                    f(0, 1)
                        f(-1, 0)
                    f(0, 2)
                        f(-1, 1) = F
                    f(0, 3)
                        f(-1, 2) = F
                    
        '''
        dp = {}

        def f(i, num_closes):
            if i < 0:
                return num_closes == 0
            if (i, num_closes) in dp:
                return dp[(i, num_closes)]
            char = s[i]
            if char == ')':
                return f(i - 1, num_closes + 1)
            elif char == '(':
                if num_closes <= 0:
                    return False
                return f(i - 1, num_closes - 1)
            else:
                res = False
                if num_closes > 0:
                    res = res or f(i - 1, num_closes - 1)
                # if it's a close
                res = res or f(i - 1, num_closes + 1)
                # if it's an empty
                res = res or f(i - 1, num_closes)
                dp[(i, num_closes)] = res
                return res

        return f(len(s) - 1, 0)