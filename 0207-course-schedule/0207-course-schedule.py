class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        [a, b] = b -> a


        {
            0: [1]
        }   
                   0, 1
        num_pre = [0, 0]
        queue: 1
        '''

        num_finish = 0
        adj_list = defaultdict(list)
        num_pre = [0] * numCourses
        queue = deque()
        
        for a, b in prerequisites:
            adj_list[b].append(a)
            num_pre[a] += 1

        for course in range(numCourses):
            if num_pre[course] == 0:
                queue.append(course)

        while queue:
            u = queue.popleft()
            num_finish += 1
            if num_finish == numCourses:
                return True
            for v in adj_list[u]:
                num_pre[v] -= 1
                if num_pre[v] == 0:
                    queue.append(v)

        return False 


        