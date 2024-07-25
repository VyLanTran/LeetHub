class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr1, arr2):
            res = []
            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            while i < len(arr1):
                res.append(arr1[i])
                i += 1
            while j < len(arr2):
                res.append(arr2[j])
                j += 1
            return res

        def binSplit(left, right):
            if left == right:
                return nums[left:right + 1]
            mid = left + (right - left) // 2
            leftArr = binSplit(left, mid)
            rightArr = binSplit(mid + 1, right)
            return merge(leftArr, rightArr)
        
        return binSplit(0, len(nums) - 1)