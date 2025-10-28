class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        0,1,2,3,4,5,6,7,8
        1,8,6,2,5,4,8,3,7
                        r
        l l
        res = 8, 49

        area = (r - l) * min(l, r)
        if l < r:
            # better to move l
        else r > l:
            # better to move r
        '''
        max_area = 0
        n = len(height)
        left, right = 0, n - 1

        while left < right:
            left_height, right_height = height[left], height[right]
            area = (right - left) * min(left_height, right_height)
            max_area = max(max_area, area)
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return max_area
