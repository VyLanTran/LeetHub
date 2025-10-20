class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        Test cases

        s = c
        p = a*
        False

        s = bd
        p = .b*d
        True because .=b, b*="", d=d

        ---
        01
        bd
        ii
        0123
        .b*d
        __jj

        {

        }

        f(1, 3)
            f(0, 2)
                F or f(0, 0) = T
                    f(-1, -1) = T
                T or f(-1, 2) = T
                    f(-1, 0) = F
        ---

        i, j points to s, p giving a, b
        f(i, j) = is it possible that s[0,i] match p[0,j]

        f(i, j)
            if (i, j) in cache:
                return that
            if i < 0:
                if j < 0:
                    return True
                if b == '*':
                    return f(i, j-2)
                return False
            if j < 0:
                return False
            if b is letter:
                if a != b:
                    return False
                return f(i-1, j-1)
            if b == '.':
                return f(i-1, j-1)
            # b == '*'
            prev_char = p[j-1]'
            if prev_char != '.' and prev_char != a:
                return f(i,j-2)
            res = False
            # 0 occurence
            res = res or f(i, j-2)
            # decide to match 1 occurence
            res = res or f(i-1,j)
            put res into cache
            return res


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