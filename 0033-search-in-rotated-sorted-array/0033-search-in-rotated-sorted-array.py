class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        no rotation:
            0, 1, 2, 3, 4 (just increasing)
        some rotations
            4, 5, 6, 7, 0, 1, 2
              / 
             /
            /
                    /
                   /
                  /
        Part A.  Part B

        if mid_val == target:
            return index
        elif mid_val < target: 
                if mid_val >= nums[0] or target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
        else:
            if mid_val < nums[0] or target >= nums[0]:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

        Time: O(log(n))
        Space: O(1)
        '''

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid
            elif mid_val < target: 
                if mid_val >= nums[0] or target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if mid_val < nums[0] or target >= nums[0]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1