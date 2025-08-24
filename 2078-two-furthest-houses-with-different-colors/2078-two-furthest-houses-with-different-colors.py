class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        '''
        {
            1: [0] -> care about min and max house for each color only
            8: [1, 3]
            3: [2, 4]
        }

        0,1,2,3,4,5
        1,8,3,8,3,1
        i         j
        return 4
        '''

        n = len(colors)

        if colors[0] != colors[-1]:
            return n - 1

        fixed_color = colors[0]
        i, j  = 1, n - 2
        while colors[i] == fixed_color and colors[j] == fixed_color:
            i += 1
            j -= 1
        
        if colors[i] != fixed_color:
            return n - 1 - i
        return j

        '''
        0,1,2,3,4,5,6
        1,1,1,6,1,1,1
          i i i
              j j j
        fixed_color = 1
        '''