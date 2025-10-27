class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        '''
     
        1, 3, 4
        2, 1, 1

        1, 2, 3, 4
        2, 0, 1, 1
        2, 2, 3, 

        i - 3, i - 2, i - 1, i

        f(i) = res if casting "power value" 1 to i
            if i < 1:
                return 0
            # if skip this power
            f(i - 1)
            # if use this power
            p * freq + f(i - 3)

            return min(f(i - 1),  p * freq + f(i - 3))

        i - 3, i - 2, i - 1
          a ,   b       c
          0

        1, 2, 4, 6, 7

        a = 0
        b = p[1] * freq[1]
        c = 

        for i from 2 to n - 1:
            pp, prev, cur
       
            if cur - prev > 2:
                res = cur + c
            else:
                if cur - pp > 2:
                    max(cur + b, c)
                else:
                    max(cur + a, b, c)
                    # max(cur + 1, c)
            a, b, c = b, c, res

        '''

        counter = Counter(power)
        power = list(set(power))
        power.sort()
        n = len(power)

        a = 0
        b = power[0] * counter[power[0]]

        if n == 1:
            return b

        c = max(b, power[1] * counter[power[1]])
        if power[1] - power[0] > 2:
            c = max(c, power[1] * counter[power[1]] + b)
        if n == 2:
            return c

        for i in range(2, n):
            pp, p, cur = power[i - 2], power[i - 1], power[i] 
            cur_damage = cur * counter[cur]
            temp = 0
            if cur - p > 2:
                temp = cur_damage + c
            else:
                if cur - pp > 2:
                    temp = max(cur_damage + b, c)
                else:
                    temp = max(cur_damage + a, c)
            a, b, c = b, c, temp

        return c
