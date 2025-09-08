class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        '''
        k = max(nums)
        Time: O(nlog(n) + nlog(k))
            - sorted: O(nlog(n))
            - binary search: O(nlog(k))
        Space: O(n) - using set
        '''

        targets = set(nums)
        targets = sorted(list(targets))
        
        def is_possible(target):
            i = 0
            houses_robbed = 0
            while i < len(nums):
                if nums[i] <= target:
                    houses_robbed += 1
                    if houses_robbed >= k:
                        return True
                    i += 2
                else:
                    i += 1
            return False

        left, right = 0, len(targets) - 1
        min_index = right
        while left <= right:
            mid = left + (right - left) // 2
            if is_possible(targets[mid]):
                min_index = mid
                right = mid - 1
            else:
                left = mid + 1
        return targets[min_index]
