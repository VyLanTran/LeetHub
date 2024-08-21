class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        inDeg = [0 for _ in range(numCourses)]
        res = []
        canTake = deque()
        
        def buildGraph():
            for second, first in prerequisites:
                graph[first].append(second)
                inDeg[second] += 1
                
        buildGraph()
        
        for i in range(numCourses):
            if inDeg[i] == 0:
                canTake.append(i)
                                
        while canTake:
            first = canTake.popleft()
            res.append(first)
            for second in graph[first]:
                inDeg[second] -= 1
                if inDeg[second] == 0:
                    canTake.append(second)
                    
        return res if len(res) == numCourses else []
        
        
            