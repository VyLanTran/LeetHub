class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or not word.isalnum():
            return False

        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        num_vowels, num_consonants = 0, 0

        for char in word:
            if char in vowels:
                num_vowels += 1
            elif char.isalpha() and char not in vowels:
                num_consonants += 1
            else:
                pass

            if num_vowels > 0 and num_consonants > 0:
                return True

        return False
            