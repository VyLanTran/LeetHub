class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        inDeg = [0, 0]
        adj = dict()
        queue = []
        count = 1
        0
        '''
        inDeg = [0 for _ in range(numCourses)]
        adj = dict()
        queue = deque()
        count = 0
        
        for i in range(numCourses):
            adj[i] = []
        
        for pre in prerequisites:
            v, u = pre[0], pre[1]
            inDeg[v] += 1
            adj[u].append(v)
            
        for i in range(numCourses):
            if inDeg[i] == 0:
                queue.append(i)
                
        # print(inDeg)
                
        while queue:
            u = queue.popleft()
            count += 1
            for v in adj[u]:
                inDeg[v] -= 1
                if inDeg[v] == 0:
                    queue.append(v)
                   
        print(count)
        return count == numCourses
            
        
        