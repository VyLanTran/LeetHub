class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        adj_list = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if j != i and isConnected[i][j] == 1:
                    adj_list[i].append(j)


        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for j in adj_list[i]:
                dfs(j)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res