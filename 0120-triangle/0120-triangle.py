class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        Time: 1 + 2 + ... + n = O(n^2) where n = triangle len
        Space: O(n)
        '''

        num_rows = len(triangle)

        prev = [triangle[0][0]]

        for i in range(1, num_rows):
            cur_row = triangle[i]
            # a new object is assigned to cur here, so won't override prev
            cur = [cur_row[0] + prev[0]]
            for j in range(1, len(cur_row) - 1):
                cur.append(cur_row[j] + min(prev[j - 1], prev[j]))
            # the right most cell is only reachable from prev[j-1]
            cur.append(cur_row[-1] + prev[-1])
            prev = cur

        return min(prev)