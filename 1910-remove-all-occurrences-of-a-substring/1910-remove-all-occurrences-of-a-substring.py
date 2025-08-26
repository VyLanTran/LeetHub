class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        '''
        daabcbaabcbc
        iiiii
                0, 1, 2, 3, 4
        stack: [d, a, a, b, c]
        '''

        stack = []

        for char in s:
            stack.append(char)
            if char == part[-1] and "".join(stack[len(stack) - len(part):len(stack)]) == part:
                for _ in range(len(part)):
                    stack.pop()
        return "".join(stack)

        