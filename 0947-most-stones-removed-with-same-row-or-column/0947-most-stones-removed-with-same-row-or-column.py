class UnionFind:
    def __init__(self):
        self.root = {}
        self.rank = {}

    def add(self, x):
        if x not in self.root:
            self.root[x] = x
            self.rank[x] = 1

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
            else:
                self.root[root_y] = root_x
                if self.rank[root_y] == self.rank[root_x]:
                    self.rank[root_x] += 1

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        row_dict = defaultdict(list)
        col_dict = defaultdict(list)
        uf = UnionFind()
        res = 0
        island_size = defaultdict(int)

        for i, j in stones:
            row_dict[i].append((i, j))
            col_dict[j].append((i, j))

        for arr in row_dict.values():
            first_vertex = arr[0]
            uf.add(first_vertex)
            for i in range(1, len(arr)):
                vertex = arr[i]
                uf.add(vertex)
                uf.union(first_vertex, vertex)

        for arr in col_dict.values():
            first_vertex = arr[0]
            uf.add(first_vertex)
            for i in range(1, len(arr)):
                vertex = arr[i]
                uf.add(vertex)
                uf.union(first_vertex, vertex)

        for i, j in stones:
            island_size[uf.find((i, j))] += 1

        for value in island_size.values():
            res += value - 1
        return res
