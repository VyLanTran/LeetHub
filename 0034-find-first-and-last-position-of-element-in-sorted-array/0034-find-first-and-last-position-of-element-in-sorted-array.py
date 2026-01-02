class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def find_target(is_first=True):
            left, right = 0, n - 1
            res = None
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    res = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1 if res is None else res

        return [find_target(), find_target(False)]
