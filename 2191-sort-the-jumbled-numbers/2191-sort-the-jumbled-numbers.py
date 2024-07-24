class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def convert(num, mapping):
            if num == 0:
                return mapping[0]
            res, power = 0, 0
            while num > 0:
                res += mapping[int(num % 10)] * pow(10, power)
                power += 1
                num = num // 10
            return res
        
        arr = [(convert(nums[i], mapping), i) for i in range(len(nums))]
        arr.sort(key=lambda x: (x[0], x[1]))
        res = [nums[arr[i][1]] for i in range(len(nums))]
        return res
        
        
                