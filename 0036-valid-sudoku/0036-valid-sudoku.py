class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Time: O(N^2) = O(1) since N = 9
        Space: O(N^2) = O(1) since N = 9
        '''
        N = 9
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        boxes = [set() for _ in range(N)]

        for i in range(N):
            for j in range(N):
                val = board[i][j]
                if val == ".":
                    continue
                box_index = (i // 3) * 3 + (j // 3)
                if val in rows[i] or val in cols[j] or val in boxes[box_index]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[box_index].add(val)
        
        return True