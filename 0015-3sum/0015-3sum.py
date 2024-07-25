class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res, n = set(), len(nums)
        nums.sort()
        for i in range(n):
            j, k = i + 1, n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return res
        
#         res, n = [], len(nums)
#         nums.sort()
#         for i in range(n):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             j, k = i + 1, n - 1
#             while j < k:
#                 sum = nums[i] + nums[j] + nums[k]
#                 if sum == 0:
#                     res.append([nums[i], nums[j], nums[k]])
#                     cur = nums[j]
#                     while j < n and nums[j] == cur:
#                         j += 1
#                     cur = nums[k]
#                     while k >= 0 and nums[k] == cur:
#                         k -= 1
#                 elif sum < 0:
#                     cur = nums[j]
#                     while j < n and nums[j] == cur:
#                         j += 1
#                 else:
#                     cur = nums[k]
#                     while k >= 0 and nums[k] == cur:
#                         k -= 1
#         return res

            
    
        