class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        
        carry = 1
        
        for i in range(len(digits) - 1, -1, -1):
            res.appendleft((digits[i] + carry) % 10)
            carry = (digits[i] + carry) // 10
        
        if carry > 0:
            res.appendleft(carry)
            
        return res  