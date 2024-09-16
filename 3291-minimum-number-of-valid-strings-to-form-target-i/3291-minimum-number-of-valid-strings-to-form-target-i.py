class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        root = TrieNode()
        dp = [float('inf') for _ in range(len(target) + 1)]
        dp[0] = 0

        def insertWord(word):
            cur = root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]

        for word in words:
            insertWord(word)

        for i in range(len(dp)):
            cur = root
            for j in range(i + 1, len(dp)):
                if target[j - 1] not in cur.children:
                    cur = root
                    break
                dp[j] = min(dp[j], 1 + dp[i])
                cur = cur.children[target[j - 1]]

        return dp[-1] if dp[-1] != float('inf') else -1



        
