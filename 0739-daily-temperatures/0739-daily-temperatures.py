class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
         0, 1 ,2 ,3 ,4 ,5 ,6, 7
        [73,74,75,71,69,72,76,73]
        [1, 1 , 0,0 ,0 ,0 ,0 ,0]
        
        
        (69, 4)
        (71, 3)
        (75, 2)
        '''
        
        stack = deque()
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][-1] < temp:
                j, lower_temp = stack.pop()
                res[j] = i - j
            stack.append((i, temp))
        return res
                