class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        arr = []
        number of opens/closes remaining to insert
        always: num_open <= num_closes

        f(num_open, num_close)
            if num_open == 0:
                turn arr into string, append ) * num_closes, then add to res
                return
            # always able to add an open
            arr.append('(')
            f(num_open - 1, num_close)
            arr.pop()
            if num_open < num_close:
                arr.append(')')
                f(num_open, num_close - 1)
                arr.pop()

        n = 2
        ()(), (())
        res = (())
        arr = [(, )] 

        f(2, 2)
            f(1, 2)
                f(0, 2) 
                    "((" + "))" 
                f(1, 1)

                
        '''

        cur_parentheses = []
        res = []

        def f(num_open, num_close):
            if num_open == 0:
                s = "".join(cur_parentheses) + ")" * num_close
                res.append(s)
                return
            # always able to add an open
            cur_parentheses.append('(')
            f(num_open - 1, num_close)
            cur_parentheses.pop()
            if num_open < num_close:
                cur_parentheses.append(')')
                f(num_open, num_close - 1)
                cur_parentheses.pop()

        f(n, n)
        return res