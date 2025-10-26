class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        '''
        0, 1, 2
        1, 6, 7
        1, 2, 1

        a = 0
        b = 1
        c = 13
        '''

        counter = Counter(power)
        power = sorted(list(set(power)))
        n = len(power)

        a = 0
        b = power[0] * counter[power[0]]
        if n == 1:
            return b
        c = power[1] * counter[power[1]]
        if power[0] + 2 < power[1]:
            c += b
        print(f'prev: {a, b, c}')
        for i in range(2, n):
            cur_damage = power[i] * counter[power[i]]
            pp_power, p_power, cur_power = power[i - 2], power[i - 1], power[i]
            temp = 0
            if p_power + 1 == cur_power: # must skip i - 1
                if pp_power + 2 == cur_power: # must skip i - 2
                    temp = max(cur_damage + a, b, c)
                else:
                    temp = max(cur_damage + b, c)
            elif p_power + 2 == cur_power: # must skip i - 1
                temp = max(cur_damage + b, c)
            else:
                temp = cur_damage + c
            a, b, c = b, c, temp

        return c

                