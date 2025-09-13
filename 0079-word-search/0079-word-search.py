class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        We should use cache, however, for the test cases available for this problem, 
        not using cache is faster

        Time: O(m * n * 3^k)
        Space: O(mnk) if we use cache
        '''
        rows, cols = len(board), len(board[0])
        # cache = {}

        def dfs(r, c, i):
            if i >= len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols):
                return False
            # if (r, c) in cache: 
            #     return cache[(r, c, i)]

            if board[r][c] != word[i]:
                # cache[(r, c, i)] = False
                return False

            board[r][c] = "*"
            res = dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1) or dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1)
            # cache[(r, c, i)] = res
            board[r][c] = word[i]
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False

