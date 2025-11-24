class UnionFind:
    def __init__(self, size):
        self.rank = [1] * size
        self.root = [i for i in range(size)]
    
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = root_y
            elif self.rank[root_y] < self.rank[root_x]:
                self.root[root_y] = root_x
            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1 




class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        uf = UnionFind(size)

        for i in range(size):
            for j in range(i + 1, size):
                if isConnected[i][j] == 1:
                    uf.union(i, j)
                    # print(f"Union {i} and {j}, root: {uf.root}, rank: {uf.rank}")

        # print(uf.root)

        '''
         0,1,2,3
        [1,0,0,1] 0
        [0,1,1,0] 1
        [0,1,1,1] 2
        [1,0,1,1] 3

        0 - 3
            |
        1 - 2
                0, 1, 2, 3
        root = [0, 1, 2, 3]
        rank = [1, 1, 1, 1]

        root(2) = 1
        root(3) = 0 
        '''
        
        roots = set()
        for i in range(size):
            roots.add(uf.find(i))
        return len(roots)

