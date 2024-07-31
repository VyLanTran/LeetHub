class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        dp = dict()
        
        def rec(n, open):
            if (n, open) in dp:
                return dp[(n, open)]
            if n == 0:
                return [")" * open]
            val = set()
            arr1 = rec(n - 1, open + 1)
            for s in arr1:
                val.add("(" + s)
            if open > 0:
                arr2 = rec(n, open - 1)
                for s in arr2:
                    val.add(")" + s)
            dp[(n, open)] = val
            return val
            
        return rec(n, 0)