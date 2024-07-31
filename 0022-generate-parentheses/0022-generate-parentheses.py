class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
#         dp = dict()
        
#         def rec(n, open):
#             if (n, open) in dp:
#                 return dp[(n, open)]
#             if n == 0:
#                 return [")" * open]
#             val = set()
#             arr1 = rec(n - 1, open + 1)
#             for s in arr1:
#                 val.add("(" + s)
#             if open > 0:
#                 arr2 = rec(n, open - 1)
#                 for s in arr2:
#                     val.add(")" + s)
#             dp[(n, open)] = val
#             return val
            
#         return rec(n, 0)

        res = []
    
        def rec(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                rec(left + 1, right, s + "(")
            if right < left:
                rec(left, right + 1, s + ")")
        rec(0, 0, "")
        return res
            
            