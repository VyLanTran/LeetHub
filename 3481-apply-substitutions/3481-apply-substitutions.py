class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        '''
        turn replacements into a dictionary
        use dp for caching

        C -> abc%B%

        f(text):
            if text not contain % (is it possible that a value contains an odd number of %)
                return text
            if text in cache:
                return that

        f(%A%_%B%_%C%)
            res = ""
            scan left to right:
                if char is not %:
                    append to res
                else:
                    get that key (just an upper case letter)
                    res += f(replacements[key])
                    skip the closing %

        replacement = f(abc%B%)
            res = abc + f(ace)

        '''

        mapping = {}
        dp = {}
        for key, val in replacements:
            mapping[key] = val

        def f(text):
            if text in dp:
                return dp[text]
            if '%' not in text:
                return text
            res = ""
            i = 0
            while i < len(text):
                char = text[i]
                if char != '%':
                    res += char
                    i += 1
                else:
                    key = text[i + 1]
                    res += f(mapping[str(key)])
                    i += 3
            dp[text] = res
            return res

        return f(text)