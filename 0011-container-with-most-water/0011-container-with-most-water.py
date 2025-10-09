class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        0,1,2,3,4,5,6,7,8
        1,8,6,2,5,4,8,3,7
        i
                        j

        V = (i - j) * min(h[i], h[j])

        if h[i] < h[j]
            i += 1
        if h[i] > h[j]:
            j = 1
        if equal
        '''

        max_area = 0
        left, right = 0, len(height) - 1

        while left <= right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        