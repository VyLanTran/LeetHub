class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        def find_target(is_first, left, right):
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

        first = find_target(True, 0, n - 1)
        if first == -1:
            return [-1, -1]
        last = find_target(False, first, n - 1)
        return [first, last]
