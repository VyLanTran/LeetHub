class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        '''
         0,  1,  2,  3
        22, 57, 74, 79

        m = 4
        '''

        position.sort()

        def is_possible(dist, num_balls):
            cur_pos = position[0]

            for i in range(1, len(position)):
                if cur_pos + dist <= position[i]:
                    # print(f'cur_pos = {cur_pos}, next_pos = {position[i]}')
                    num_balls -= 1
                    cur_pos = position[i]
                    if num_balls == 1:
                        return True
            
            return False

        if m == 2:
            return position[-1] - position[0]

        left, right = 1, position[-1] - position[0]
        max_force = 1
        while left <= right:
            mid = left + (right - left) // 2
            if is_possible(mid, m):
                max_force = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return max_force
        # print(position)
        # print(is_possible(35, 4))        