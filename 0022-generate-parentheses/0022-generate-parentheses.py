class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        f( open_count, close_count)
            if both = 0:
                join to make a string then append to res
                return
            if open_count > 0:
                arr.append("(")
                f(, open_count - 1, close_count)
                arr.pop()
            if open_count < n:
                arr.append(")")
                f(, open_count, close_count - 1)
                arr.pop()

        res = "((()))"
        arr = (, (, (, ), )
        f(3, 3)
            f(2, 3)
                f(1, 3)
                    f(0, 3)
                        f(0, 2)
                            f(0, 1)
                                f(0, 0) => "((()))"

        '''

        res = []
        arr = []

        def rec(open_count, close_count):
            if open_count < 0 or close_count < 0:
                return
            if open_count == 0 and close_count == 0:
                res.append("".join(arr))
                return
            if open_count > 0:
                arr.append("(")
                rec(open_count - 1, close_count)
                arr.pop()
            if close_count > open_count:
                arr.append(")")
                rec(open_count, close_count - 1)
                arr.pop()

        rec(n, n)

        return res