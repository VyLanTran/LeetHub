class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''
        Time: O(m + n)
        Space: O(1)
        '''

        i, j, k = m - 1, n - 1, m + n - 1

        while k >= 0:
            num1 = nums1[i] if i >= 0 else float('-inf')
            num2 = nums2[j] if j >= 0 else float('-inf')
            if num1 > num2:
                nums1[k] = num1
                i -= 1
            else:
                nums1[k] = num2
                j -= 1
            k -= 1
