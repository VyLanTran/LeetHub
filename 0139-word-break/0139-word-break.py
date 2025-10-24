class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def build_tree():
            root = TrieNode()
            for word in wordDict:
                cur = root
                for i, char in enumerate(word):
                    if char not in cur.children:
                        cur.children[char] = TrieNode()
                    cur = cur.children[char]
                cur.is_word = True
            return root

        root = build_tree()
        dp = {-1: True}

        def is_word(start, end):
            if start >= len(s) or end >= len(s):
                return False
            cur = root
            for i in range(start, end + 1):
                char = s[i]
                if char not in cur.children:
                    return False
                cur = cur.children[char]
            return cur.is_word

        def f(i):
            if i < 0:
                return True
            if i in dp:
                return dp[i]
            for j in range(i + 1):
                if is_word(j, i):
                    if f(j - 1):
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        # res =  f(len(s) - 1)
        # print(dp)
        # return res
        return f(len(s) - 1)

        # print(is_word(4, 7))