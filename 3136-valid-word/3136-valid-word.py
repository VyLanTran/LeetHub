class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3 or not word.isalnum():
            return False

        vowels = set(['a', 'e', 'i', 'o', 'u'])
        has_vowel, has_consonant = False, False

        for char in word:
            if char.isalpha():
                char = char.lower()
                if char in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
                
                if has_vowel and has_consonant:
                    return True
            elif not char.isnumeric():
                return False

            
        return False