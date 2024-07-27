class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        print(nums1, nums2)
        
        def isValid(start, nums1, nums2):
            i, j = start, 0
            numRemove, diff = 0, nums2[0] - nums1[i]
            while j < len(nums2) and i < len(nums1):
                print(i, j, nums1[i], nums2[j], diff)
                if nums2[j] - nums1[i] != diff:
                    # print(i, j, nums1[i], nums2[j], nums2[j] - nums1[i] )
                    i += 1
                    numRemove += 1
                    if numRemove > 2 - start:
                        break
                else:
                    j += 1
                    i += 1
            # print("here", numRemove, 2 - start)
            numRemove += len(nums1) - i
            return numRemove == 2 - start
        
        # print(isValid(0, nums1, nums2))
        
        res = None
        for i in range(0, 3):
            if isValid(i, nums1, nums2):
                newDiff = nums2[0] - nums1[i]
                # if not res or abs(res) > abs(newDiff) or (abs(res) == abs(newDiff) and newDiff < res):
                #     res = newDiff
                res = min(res, newDiff) if res else newDiff
        print(isValid(0, nums1, nums2))
        
        return res
        # return 0
        
        
                
                