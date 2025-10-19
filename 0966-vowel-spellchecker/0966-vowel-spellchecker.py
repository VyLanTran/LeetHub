class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        n, m = len(wordlist), len(queries)
        exact_matches = set(wordlist)
        capitalization_matches = {}
        vowel_matches = {}

        def hide_vowel(word):
            vowel_hidden = ""
            for i, char in enumerate(word):
                vowel_hidden += "*" if char in "aeiou" else char
            return vowel_hidden

        for word in wordlist:
            word_lower = word.lower()
            if word_lower not in capitalization_matches:
                capitalization_matches[word_lower] = word
            vowel_hidden = hide_vowel(word_lower)
            if vowel_hidden not in vowel_matches:
                vowel_matches[vowel_hidden] = word

        for i, word in enumerate(queries):
            if word in exact_matches:
                queries[i] = word
                continue
            word_lower = word.lower()
            if word_lower in capitalization_matches:
                queries[i] = capitalization_matches[word_lower]
                continue
            vowel_hidden = hide_vowel(word_lower)
            if vowel_hidden in vowel_matches:
                queries[i] = vowel_matches[vowel_hidden]
                continue
            queries[i] = ""

        return queries
