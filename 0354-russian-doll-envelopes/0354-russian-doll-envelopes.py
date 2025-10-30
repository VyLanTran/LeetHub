class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort(key=lambda x:[x[0], -x[1]])
        increasing_heights = [envelopes[0][1]]

        for i in range(1, n):
            height = envelopes[i][1]
            if height > increasing_heights[-1]:
                increasing_heights.append(height)
            else:
                index = bisect.bisect_left(increasing_heights, height)
                increasing_heights[index] = height
        return len(increasing_heights)

    