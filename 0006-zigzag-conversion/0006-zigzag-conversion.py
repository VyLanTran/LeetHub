class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        Time: O(n)
        Space: O(n)
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