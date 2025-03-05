class Solution:
    def greatestLetter(self, s: str) -> str:
        upperCount = [0] * 26
        lowerCount = [0] * 26

        for char in s:
            if char.islower():
                lowerCount[ord(char) - ord('a')] = 1
            else:
                upperCount[ord(char) - ord('A')] = 1

        for i in range(25, -1, -1):
            if upperCount[i] + lowerCount[i] == 2:
                return chr(ord('A') + i) + ""

        return ""
