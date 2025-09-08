class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        '''
        m = max(nums)
        Time: O(mlog(n))
        Space: O(1)
        '''

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

        left, right = 1, max(nums)
        best_target = right

        while left <= right:
            mid = left + (right - left) // 2
            if is_possible(mid):
                best_target = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return best_target

        '''
        k = max(nums)
        Time: O(nlog(n) + nlog(k))
            - sorted: O(nlog(n))
            - binary search: O(nlog(k))
        Space: O(n) - using set

        Actually, we don't need targets
        Initial thoughts: if we find best_target but best_target is not in nums
        But why this is not possible?

        is_possible(best_target) = True
        => all chosen houses <= best_target
        actually all chosen houses <= max(all chosen houses)
        => we can choose that as best_target
        => can always narrow down to that value, which guaranteed to be in nums

        '''

        # targets = set(nums)
        # targets = sorted(list(targets))
        
        # def is_possible(target):
        #     i = 0
        #     houses_robbed = 0
        #     while i < len(nums):
        #         if nums[i] <= target:
        #             houses_robbed += 1
        #             if houses_robbed >= k:
        #                 return True
        #             i += 2
        #         else:
        #             i += 1
        #     return False

        # left, right = 0, len(targets) - 1
        # min_index = right
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if is_possible(targets[mid]):
        #         min_index = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return targets[min_index]
