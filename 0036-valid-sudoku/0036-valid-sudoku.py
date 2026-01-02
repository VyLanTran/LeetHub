class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
         0 1 2 3 4 5 6 7 8 9
        0
        1
        2
        3
        4
        5

        (2, 2): 0

        0, 0 -> 0
        1, 0 -> 3
        1, 2 -> 5
        2, 2 -> 8 = 2 * 3 + 2

        8 -> 2 = 8//3
        1 -> 3
        ''' 

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        SIZE = 9

        for i in range(SIZE):
            for j in range(SIZE):
                char = board[i][j]
                if char == ".":
                    continue
                if char in rows[i] or char in cols[j] or char in boxes[(i // 3) * 3 + j // 3]:
                    return False
                rows[i].add(char)
                cols[j].add(char)
                boxes[(i // 3) * 3 + j // 3].add(char)

        return True