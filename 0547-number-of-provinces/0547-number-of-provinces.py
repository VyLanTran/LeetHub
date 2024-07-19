class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False for _ in range(n)]

        def dfs(i):
            for j in range(n):
                if j != i and isConnected[i][j] and not visited[j]:
                    visited[j] = True
                    dfs(j)

        count = 0
        for x in range(n):
            if not visited[x]:
                visited[x] = True
                dfs(x)
                count += 1
            
        return count