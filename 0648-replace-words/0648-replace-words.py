class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        
        def insert(word):
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.endOfWord = True
   
        def findRoot(word):
            cur = root
            path = ""
            i = 0
            while i < len(word):
                c = word[i]
                if c not in cur.children:
                    break
                path += c
                cur = cur.children[c]
                if cur.endOfWord:
                    return path
                i += 1
            if i < len(word):
                path += word[i:]
            return path
        
        for word in dictionary:
            insert(word)
            
        i = 0
        res = ""
        curWord = ""
        while i < len(sentence):
            c = sentence[i]
            if c == " ":
                res += c
            else:
                curWord += c
                if i == len(sentence) - 1 or sentence[i + 1] == " ":
                    res += findRoot(curWord)
                    curWord = ""
            i += 1
        
        return res
            
        
        