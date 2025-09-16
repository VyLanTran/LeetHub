class Solution:
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        '''
        n = number of nodes
        m = number of edges

        Time: O(m)
        Space: O(m)
        '''
        max_count = 1

        def create_graph():
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append((v, colors[v]))
            return graph

        graph = create_graph()

        def dfs(node):
            if node not in graph:
                return 1, True

            nonlocal max_count
            color = colors[node]
            is_valid_tree = True
            tree_size = 1
            
            for child, child_color in graph[node]:
                subtree_size, is_valid_subtree = dfs(child)
                is_valid_tree = is_valid_tree and child_color == color and is_valid_subtree
                tree_size += subtree_size

            if is_valid_tree:
                max_count = max(max_count, tree_size)
            
            return tree_size, is_valid_tree

        dfs(0)

        return max_count