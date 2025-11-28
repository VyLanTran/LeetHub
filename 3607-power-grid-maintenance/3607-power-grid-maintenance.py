class UnionFind:
    def __init__(self, size):
        self.rank = [1] * (size + 1)
        self.root = [i for i in range(size + 1)]
    
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

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        uf = UnionFind(c)
        root_to_online = defaultdict(list)
        is_online = [True] * (c + 1)
        res = []

        for i, j in connections:
            uf.union(i, j)

        for i in range(1, c + 1):
            root = uf.find(i)
            heappush(root_to_online[root], i)

        for request_type, x in queries:
            if request_type == 2:
                is_online[x] = False
            else:
                if is_online[x]:
                    res.append(x)
                    continue
                root = uf.find(x)
                stations = root_to_online[root]
                while stations and not is_online[stations[0]]:
                    heappop(stations)
                if not stations:
                    res.append(-1)
                else:
                    res.append(stations[0])

        return res


                

        