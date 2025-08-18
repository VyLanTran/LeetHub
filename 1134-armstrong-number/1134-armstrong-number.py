class Solution:
    def isArmstrong(self, n: int) -> bool:
        origin_val = n
        power = len(str(n))
        digit_sum = 0
        while n > 0:
            digit_sum += (n % 10) ** power
            n //= 10
        return digit_sum == origin_val