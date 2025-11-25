class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                if self.rank[root_x] == self.rank[root_y]:
                    self.rank[root_x] += 1
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        '''
        that happens when all nodes are connected into one island

        0, 1 
        '''
        logs.sort(key=lambda x: x[0])
        num_sets = n
        uf = UnionFind(n)

        for time, i, j in logs:
            if not uf.is_connected(i, j):
                uf.union(i, j)
                num_sets -= 1
                if num_sets == 1:
                    return time
        return -1
