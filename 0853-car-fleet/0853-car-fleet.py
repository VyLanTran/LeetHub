class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pairs = [(position[i], (target - position[i]) / speed[i]) for i in range(n)]
        pairs.sort(key=lambda x:x[0])
        stack = []
        for i in range(n):
            time = pairs[i][-1]
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        return len(stack)