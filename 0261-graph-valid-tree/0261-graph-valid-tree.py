class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
        def createGraph():
            graph = defaultdict(list)
            for i, j in edges:
                graph[i].append(j)
                graph[j].append(i)
            return graph
        
        graph = createGraph()
        visited = set()
        isValid = True
        
        def dfs(i, prev):
            nonlocal isValid
            if not isValid:
                return
            if i in visited:
                isValid = False
                return
            visited.add(i)
            for j in graph[i]:
                if j != prev:
                    dfs(j, i)
                
        dfs(0, None)
        return isValid and len(visited) == n
            