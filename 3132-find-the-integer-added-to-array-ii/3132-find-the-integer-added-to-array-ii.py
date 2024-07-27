class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
                
        def isValid(start, nums1, nums2):
            i, j = start, 0
            numRemove, diff = 0, nums2[0] - nums1[i]
            while j < len(nums2) and i < len(nums1):
                if nums2[j] - nums1[i] != diff:
                    i += 1
                    numRemove += 1
                    if numRemove > 2 - start:
                        break
                else:
                    j += 1
                    i += 1
            numRemove += len(nums1) - i
            return numRemove == 2 - start
                
        res = None
        for i in range(0, 3):
            if isValid(i, nums1, nums2):
                newDiff = nums2[0] - nums1[i]
                res = min(res, newDiff) if res else newDiff
        
        return res
        
        
                
                