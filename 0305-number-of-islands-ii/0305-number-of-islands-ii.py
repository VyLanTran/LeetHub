class UnionFind:
    def __init__(self):
        self.root = {}
        self.rank = {}

    def insert(self, x):
        self.root[x] = x
        self.rank[x] = 1

    def find(self, x):
        # find root of node x, assume that x does exist
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return 
        if self.rank[root_x] == self.rank[root_y]:
            self.root[root_y] = root_x
            self.rank[root_x] += 1
        elif self.rank[root_x] < self.rank[root_y]:
            self.root[root_x] = root_y
        else:
            self.root[root_y] = root_x

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        island_map = {}
        res = []
        island_id = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        num_islands = 0
        uf = UnionFind()

        for i, j in positions:
            if (i, j) in island_map:
                res.append(num_islands)
                continue
            adjacent_islands = set()
            for di, dj in dirs:
                new_i, new_j = i + di, j + dj
               
                if (not (0 <= new_i < m and 0 <= new_j < n)) or ((new_i, new_j) not in island_map):
                    continue
                root_island = uf.find(island_map[(new_i, new_j)])
                adjacent_islands.add(root_island)
                
            adjacent_islands = list(adjacent_islands)
            if len(adjacent_islands) == 0:
                island_map[(i, j)] = island_id
                uf.insert(island_id)
                island_id += 1
                num_islands += 1
            elif len(adjacent_islands) == 1:
                island_map[(i, j)] = adjacent_islands[0]
            else:
                cur_island = None
                for island in adjacent_islands:
                    if cur_island is None:
                        cur_island = island
                    else:
                        uf.union(cur_island, island)
                island_map[(i, j)] = adjacent_islands[0]
                num_islands -= (len(adjacent_islands) - 1)

            res.append(num_islands)

        return res