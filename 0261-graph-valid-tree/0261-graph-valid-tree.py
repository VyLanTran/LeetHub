class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        valid if:
        - no cycle
        - one island

        f(0)
            f(1)
                f(2)
                    f(3)

        '''

        visited = set()
        adj_list = defaultdict(list)

        for i, j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)

        def dfs(i, parent):
            if i in visited:
                return False
            visited.add(i)
            for j in adj_list[i]:
                if j != parent:
                    if not dfs(j, i):
                        return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
