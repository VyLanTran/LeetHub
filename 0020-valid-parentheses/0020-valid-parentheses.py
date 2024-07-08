from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        map = { ')': '(',  '}': '{',  ']': '['}
        stack = deque()
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                continue
            if len(stack) == 0 or stack.pop() != map[c]:
                return False
        return len(stack) == 0
            
            