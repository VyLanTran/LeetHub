class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        '''
        k = max position - min position
        n = number of baskets

        Time: O(nlog(k) + nlog(n)) 
        Space: O(1)
        '''

        position.sort()

        def is_possible(dist, num_balls):
            cur_pos = position[0]

            for i in range(1, len(position)):
                if cur_pos + dist <= position[i]:
                    num_balls -= 1
                    cur_pos = position[i]
                    if num_balls == 1:
                        return True
            
            return False

        if m == 2:
            return position[-1] - position[0]

        '''
        right = (position[-1] - position[0]) // (m - 1) 
        this is a stricter bound to optimize binary search
        this formula is how we calculate maximum min force between 2
        consecutive balls - which happens supposed (ideally) that the 
        baskets are evenly distributed, ie, any 2 consecutive baskets
        maintain a fixed distance = total distance between first and last basets / number of spaces in between, ie, m - 1
        '''
        left, right = 1, (position[-1] - position[0]) // (m - 1)
        max_force = 1
        while left <= right:
            mid = left + (right - left) // 2
            if is_possible(mid, m):
                max_force = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return max_force       

     