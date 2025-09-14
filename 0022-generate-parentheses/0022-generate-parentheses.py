class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
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