class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ""
        i, count, curString = len(s) - 1, 0, ""
        
        while i >= 0:
            char = s[i]
            if char == '-':
                pass
            else:
                curString = char.upper() + curString
                count += 1
                if count == k:
                    res = curString if not res else curString + "-" + res
                    curString, count = "", 0
            i -= 1
        if curString:
            return curString if not res else curString + "-" + res
        return res
    
    '''
    2-5g-3-J
    iiiiiiii         
    
    res = -5G-3J
    curString = 2
    count = 1
    '''