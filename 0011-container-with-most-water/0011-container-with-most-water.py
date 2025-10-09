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
        left, right = 0, len(height) - 1

        while left <= right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
        