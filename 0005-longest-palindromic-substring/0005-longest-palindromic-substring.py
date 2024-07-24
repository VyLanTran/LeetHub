class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 1
        res = s[0]
        
        for i in range(len(s)):
            oddIndex, evenIndex = i, i + 0.5
            oddGap, evenGap = 1, 0.5
            # print(evenIndex - evenGap, evenIndex + evenGap)
            while oddIndex - oddGap >= 0 and oddIndex + oddGap < len(s) and s[oddIndex - oddGap] == s[oddIndex + oddGap]:
                oddGap += 1
            while evenIndex - evenGap >= 0 and evenIndex + evenGap < len(s) and s[int(evenIndex - evenGap)] == s[int(evenIndex + evenGap)]:
                evenGap += 1
            oddGap, evenGap = oddGap - 1, evenGap - 1
            if 2*oddGap + 1 > maxLen:
                maxLen = 2*oddGap + 1
                res = s[oddIndex-oddGap : oddIndex+oddGap+1]
            if 2*evenGap + 1 > maxLen:
                maxLen = 2*evenGap + 1
                res = s[int(evenIndex-evenGap) : int(evenIndex+evenGap+1)]
        return res