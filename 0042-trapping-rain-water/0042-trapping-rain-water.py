class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11
        0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1
        X, 0, 1, 0, 1, 2, 1, 0, 1, 2, 1, 2
        _, _, _, _, _, _, _, 0, 0, 1, 0, X

        left_height = 0, 1, 2, 3
        amount = left_height - cur_height 
        right_height = 2, 2, 3

        left -> right until we see a height >= cur
        take the min of (left, right)

        0, 1, 2, 3, 4, 5, 6, *, 8, 9,10,11
        0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1
        0, 0, 1, 0, 1, 2, 1, 0, _, _, _, _
        _, _, _, _, _, _, _, 0, 0, 1, 0, 0 
        
        '''
        n = len(height)
        first_max_left, first_max_right = 0, n - 1
        res = 0

        for i in range(n):
            if height[i] > height[first_max_left]:
                first_max_left = i
        for i in range(n - 1, -1, -1):
            if height[i] > height[first_max_right]:
                first_max_right = i
        
        max_left_height = height[0]
        for i, h in enumerate(height):
            if i == first_max_right:
                break
            if h > max_left_height:
                max_left_height = h
            else:
                res += max_left_height - h
        
        max_right_height = height[-1]
        for i in range(n - 1, -1, -1):
            h = height[i]
            if i == first_max_left:
                break
            if h > max_right_height:
                max_right_height = h
            else:
                res += max_right_height - h

        return res

        