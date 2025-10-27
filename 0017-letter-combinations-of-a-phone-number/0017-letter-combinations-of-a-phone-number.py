class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        "23"
         i

        arr = [a, d]
        f(i = 0)
            options: abc
            append a
                f(i = 1)
                    options: def
                    append d
                        f(i = 2)
                            res.append(deepcopy(arr))
                    remove d
                    appende
        '''

        res = []
        n = len(digits)
        letters = []
        mapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        def f(i):
            if i >= n:
                res.append("".join(letters))
                return
            digit = digits[i]
            for letter in mapping[digit]:
                letters.append(letter)
                f(i + 1)
                letters.pop()
        
        f(0)
        return res
