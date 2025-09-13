class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        cache = {}

        def dfs(r, c, i):
            if i >= len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            if (r, c) in cache: 
                return cache[(r, c, i)]

            if board[r][c] != word[i]:
                cache[(r, c, i)] = False
                return False

            visited_char = board[r][c]
            board[r][c] = "*"
            res = dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1)
            cache[(r, c, i)] = res
            board[r][c] = visited_char
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

