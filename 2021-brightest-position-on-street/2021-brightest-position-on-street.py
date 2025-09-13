class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        ''' -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6
        ------------------
                        --------------
                            -------------------
                                -------------
        -5: 1
        0: 0
        -1: 1
        4: -1
        7: -1
        1:  1
        6: -1

        sort by key
        -5, -1, 0, 1, 4, 6, 7
         1,  1, 0, 1,-1,-1,-1
    0,   1,  2, 2, 3, 2, 1, 0    
        '''

        map = defaultdict(int)
        max_light, max_pos = 0, 0
        cur_light = 0

        for center, width in lights:
            start, end = center - width, center + width
            map[start] += 1
            map[end + 1] -= 1
        
        pairs = list(map.items())
        pairs.sort(key=lambda x:x[0])

        for key, val in pairs:
            cur_light += val
            if cur_light > max_light:
                max_light = cur_light
                max_pos = key

        return max_pos