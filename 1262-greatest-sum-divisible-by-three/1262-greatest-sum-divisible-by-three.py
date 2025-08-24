class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        '''
        sum = sum of all nums
        find remainder of sum
        if rem == 0:
            return sum
        if rem == 1:
            find the smallest sum with remainder = 1
            1 = 1 + (0)
              = 2 + 2 + (0)
            => must exist at least 1 number with rem = 1 or 2 numbers with rem = 2
        if rem == 2:
            find min sum with rem = 2
            2 = 1 + 1 + (0)
                = 2 + (0)

         6, 10, 12, 1, 2, 3,1
         find 2 min numbers with rem =1 (1, 1)
         two_min = [10, inf]
         if num <= two_min[0]:
            two_min[1], two_min[0] = two_min[0], num
         elif num < two_min[1]:
            two_min[1] = num
        '''

        total = sum(nums)

        
        
        def find_min_subtract(count1, count2):
            # return <count1> numbers with rem = 1 and <count2> number with rem = 2
            group1, group2 = [float('inf'), float('inf')],[float('inf'), float('inf')] 

            for num in nums:
                if num % 3 == 1:
                    if num <= group1[0]:
                        group1[1], group1[0] = group1[0], num
                    elif num < group1[1]:
                        group1[1] = num
                elif num % 3 == 2:
                    if num <= group2[0]:
                        group2[1], group2[0] = group2[0], num
                    elif num < group2[1]:
                        group2[1] = num
            
            if count1 == 1:
                return min(group1[0], sum(group2))
            return min(group2[0], sum(group1))
            
        if total % 3 == 0:
            return total
        elif total % 3 == 1:
            return total - find_min_subtract(1, 2)
        return total - find_min_subtract(2, 1)
              