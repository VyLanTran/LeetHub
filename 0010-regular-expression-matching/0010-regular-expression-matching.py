class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Time: O(mn)
        Space: O(mn)
        
        Test cases

        s = c
        p = a*
        False

        s = bd
        p = .b*d
        True because .=b, b*="", d=d
        '''
        m, n = len(s), len(p)
        dp = {}


        def f(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            a, b = s[i], p[j]
            if i < 0:
                if j < 0:
                    return True
                if b == '*':
                    return f(i, j-2)
                return False
            if j < 0:
                return False
            if b.isalpha():
                if a != b:
                    return False
                return f(i-1, j-1)
            if b == '.':
                return f(i-1, j-1)

            prev_char = p[j-1]
            if prev_char != '.' and prev_char != a:
                # must be 0 occurence of prev_char
                return f(i, j-2)
            res = False
            # 0 occurence
            res = res or f(i, j-2)
            # 1 occurence
            res = res or f(i-1, j)
            
            dp[(i, j)] = res
            return res

        return f(m - 1, n - 1)