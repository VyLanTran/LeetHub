class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        '''
        
        '''
        freq = dict()
        specialWords = set()
        visited = set()
        res = 0
        
        for word in words:
            freq[word] = freq.get(word, 0) + 1
            if word[0] == word[1]:
                specialWords.add(word)
                
        # print(freq, specialWords)
                
        for word in freq:
            if word in specialWords:
                continue
            palindrome = word[1] + word[0]
            if palindrome not in freq or palindrome in visited:
                continue
            res += min(freq[word], freq[palindrome]) * 4
            visited.add(word)
            visited.add(palindrome)
            
        if not specialWords:
            return res
        
        containsMiddleWord = False
        for word in specialWords:
            if freq[word] % 2 == 1:
                containsMiddleWord = True
                # print("here")
            if freq[word] > 1:
                res += (freq[word] // 2) * 4
        # print(res)
        if containsMiddleWord:
            res += 2
        return res
            
            
            
            