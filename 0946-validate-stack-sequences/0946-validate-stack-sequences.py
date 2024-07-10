class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j, size = 0, 0, len(pushed)
        stack = deque()
        
        while j < size:
            if len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                continue
            if i >= size:
                return False
            stack.append(pushed[i])
            i += 1
            
        return True
            
            