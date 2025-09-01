class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        V = number of vertices (courses)
        E = number of edges (len of prerequisites)

        Time: O(V + E)
            Note: for the while loop, we actually go through each nodes and edge at most once => O(E + V)
        Space: O(V + E)
        '''

        num_taken = 0
        queue = deque()
        in_degree = [0 for _ in range(numCourses)]
        graph = defaultdict(list)

        for next_course, prev_course in prerequisites:
            in_degree[next_course] += 1
            graph[prev_course].append(next_course)

        for i, val in enumerate(in_degree):
            if val == 0:
                queue.append(i)

        while queue:
            course = queue.popleft()
            num_taken += 1

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return num_taken == numCourses
