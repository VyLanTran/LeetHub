class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        '''
        0123
        RR.L
        
        fallingOrFallen = {0, 1, 3}
        t = 0
        ()
        considering: (2: 0 + 1 - 1 = 0)
        
        
        01234567890123
        .L.R...LR..L..
        LL_RR_LLRRLL__
        fallingOrFallen = {1, 3, 7, 8, 11, 0, 4, 6, 9, 10}
        
        t = 0
        
        
        considering:
        0: 0 - 1
        4: 0 + 1
        6: 0 - 1
        9: 0 + 1
        10: 0 - 1
        
        5: 0 + 1 - 1
        '''
        
        n = len(dominoes)
        res = ["." for _ in range(n)]
        
        fallingOrFallen = set()
        queue = deque()
        
        for i in range(n):
            c = dominoes[i]
            if c == "L":
                fallingOrFallen.add(i)
                queue.append((i, -1))
            elif c == "R":
                fallingOrFallen.add(i)
                queue.append((i, 1))
        while queue:
            size = len(queue)
            direction = dict()
            for _ in range(size):
                (i, d) = queue.popleft()
                res[i] = "L" if d == -1 else "R"
                j = i + d
                if j >= 0 and j < n and j not in fallingOrFallen:
                    direction[j] = direction.get(j, 0) + d
            for i, d in direction.items():
                if d == 0:
                    continue
                res[i] = "L" if d == -1 else "R"
                queue.append((i, d))
                fallingOrFallen.add(i)
                
        return ''.join(res)