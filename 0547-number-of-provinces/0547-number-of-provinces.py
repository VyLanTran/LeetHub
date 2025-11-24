class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # DFS
        # create adj list
        adj_list = defaultdict(list)
        num_vertices = len(isConnected)
        visited = set()
        res = 0

        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if isConnected[i][j] == 1:
                    adj_list[i].append(j)
                    adj_list[j].append(i)
        def dfs(i):
            visited.add(i)
            for j in adj_list[i]:
                if j not in visited:
                    dfs(j)

        
        for i in range(num_vertices):
            if i not in visited:
                dfs(i)
                res += 1
        return res
