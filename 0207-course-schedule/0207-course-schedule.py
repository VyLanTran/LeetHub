class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def createGraph():
            graph = defaultdict(list)
            inDegrees = [0] * numCourses
            for after, before in prerequisites:
                graph[before].append(after)
                inDegrees[after] += 1
            return graph, inDegrees
        
        
        graph, inDegrees = createGraph()     
        queue = deque()
        numTaken = 0
        
        for i in range(numCourses):
            if inDegrees[i] == 0:
                queue.append(i)
                
        while queue:
            size = len(queue)
            for _ in range(size):
                i = queue.popleft()
                numTaken += 1
                for j in graph[i]:
                    inDegrees[j] -= 1
                    if inDegrees[j] == 0:
                        queue.append(j)
                        
        return numTaken == numCourses