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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        island_to_heap = {}
        res = []

        for i, j in pairs:
            uf.union(i, j)

        for i, char in enumerate(s):
            root = uf.find(i)
            if root not in island_to_heap:
                island_to_heap[root] = []
            heappush(island_to_heap[root], char)

        for i in range(n):
            root = uf.find(i)
            res.append(heappop(island_to_heap[root]))

        return "".join(res)

        