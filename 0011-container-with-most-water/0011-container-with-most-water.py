class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        Time: O(n)
        Space: O(1)
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
