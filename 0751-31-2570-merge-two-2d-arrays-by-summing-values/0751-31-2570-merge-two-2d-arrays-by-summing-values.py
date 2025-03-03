class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        len1, len2 = len(nums1), len(nums2)
        i, j = 0, 0
        res = []

        while i < len1 or j < len2:
            if i >= len1:
                id1 = float('inf')
            else:
                id1, val1 = nums1[i]

            if j >= len2:
                id2 = float('inf')
            else:
                id2, val2 = nums2[j]

            if id1 == id2:
                res.append([id1, val1 + val2])
                i += 1
                j += 1
            elif id1 < id2:
                res.append([id1, val1])
                i += 1
            else:
                res.append([id2, val2])
                j += 1

        return res

        '''
        [[1,2],[2,3],[4,5]]
          i.   i.     i.    i
 
        [1,4],[3,2],[4,1]
         j.   j.    j.    j

        res = [1, 6], [2, 3], [3, 2], [4, 6]

        id1 = 1
        id2 = 1
        val1 = 2
        val2 = 4
        '''

