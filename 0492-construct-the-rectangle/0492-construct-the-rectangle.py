class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = floor(sqrt(area))
        while True:
            if area % width == 0:
                return [area//width, width]
            width -= 1
        