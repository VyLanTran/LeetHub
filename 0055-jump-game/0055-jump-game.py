class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        l, r = 0, 0

        while r < n - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            if furthest == r:
                print(l, r, furthest)
                return False
            l, r = r + 1, furthest
        return True
