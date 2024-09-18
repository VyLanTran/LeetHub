from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(num1, num2):
            return 1 if num1 + num2 >= num2 + num1 else -1
        
        def removeLeadingZeros(s):
            i = 0
            while i < len(s) and s[i] == '0':
                i += 1
            if i >= len(s):
                return "0"
            return s[i:len(s)]
        
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(compare), reverse=True)
        return removeLeadingZeros(''.join(nums))
        
        
                 