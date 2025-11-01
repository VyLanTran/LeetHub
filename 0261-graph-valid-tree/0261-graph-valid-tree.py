class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        0 1 2 3 4
        _ _ _ _ _

        f(0, prev = None)
        '''

        adj_list = defaultdict(list)
        visited = set()

        # build adj_list
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def contains_cycle(node, prev):
            if node in visited:
                return True
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor != prev:
                    if contains_cycle(neighbor, node):
                        return True
            return False

        if contains_cycle(0, None):
            return False
        return len(visited) == n
        
