class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minNeg, maxPos, res = None, None, nums[0]
        for num in nums:
            if num == 0:
                res = max(res, num)
                newMinNeg, newMaxPos = None, None
            elif num > 0:
                curMax = num * maxPos if maxPos else num
                res = max(res, curMax)
                newMaxPos = num * maxPos if maxPos else num
                newMinNeg = num * minNeg if minNeg else None
            else:
                curMax = num * minNeg if minNeg else num
                res = max(res, curMax)
                newMaxPos = num * minNeg if minNeg else None
                newMinNeg = num * maxPos if maxPos else num
            maxPos, minNeg = newMaxPos, newMinNeg

        return res