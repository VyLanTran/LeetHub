class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b): 
            if a + b > b + a:
                return -1
            return 1
        
        nums = [str(num) for num in nums]
        nums = sorted(nums, key = cmp_to_key(compare))
        return "0" if nums[0] == "0" else "".join(nums)