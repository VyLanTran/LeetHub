class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        num_pre = [0] * numCourses
        queue = deque()
        res = []

        for a, b in prerequisites:
            adj_list[b].append(a)
            num_pre[a] += 1
        
        for i in range(numCourses):
            if num_pre[i] == 0:
                queue.append(i)

        while queue:
            u = queue.popleft()
            res.append(u)
            for v in adj_list[u]:
                num_pre[v] -= 1
                if num_pre[v] == 0:
                    queue.append(v)

        return [] if len(res) < numCourses else res