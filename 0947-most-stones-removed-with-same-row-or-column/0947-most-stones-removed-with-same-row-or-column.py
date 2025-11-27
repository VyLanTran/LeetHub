class UnionFind:
    def __init__(self, vertices):
        self.root = {(x, y): (x, y) for x, y in vertices}
        self.rank = defaultdict(lambda: 1)

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

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        '''
        Fact: a disjoint set with n components -> we can delete all but 1 component
        Given n stones
        Let say they form k disjoint sets 
        Then there are k points remaining
        => res = n - k

        Problem becomes counting number of disjoint sets (similar to number of provinces)
        '''
        n = len(stones)
        num_sets = n
        uf = UnionFind(stones)

        for i in range(n):
            x1, y1 = stones[i]
            for j in range(i + 1, n):
                x2, y2 = stones[j]
                if (x1 == x2 or y1 == y2) and not uf.is_connected((x1, y1), (x2, y2)):
                    uf.union((x1, y1), (x2, y2))
                    num_sets -= 1

        return n - num_sets

