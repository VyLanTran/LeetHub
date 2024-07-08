class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                tup = stack.pop()
                res[tup[1]] = i - tup[1]
            stack.append((temperatures[i], i))
        
        return res