class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        PAYPALISHIRING
        01210

        0: []
        1: []
        2: []

        cur_row = 0
        direction = 1
        i: 0 to n-1
            add s[i] to map[cur_row]
            if dir == 1 and cur_row == n - 1:
                dir = -dir
            elif dir == -1 and cur_row == 0:
                dir = -dir

            cur_row += dir
        '''

        if numRows == 1:
            return s

        cur_row, direction = 0, 1
        map = defaultdict(list)
        arr = []

        for i in range(len(s)):
            map[cur_row].append(s[i])
            if (cur_row == numRows - 1 and direction == 1) or (cur_row == 0 and direction == -1):
                direction = -direction
            cur_row += direction

        for row in range(numRows):
            arr.extend(map[row])

        return "".join(arr)