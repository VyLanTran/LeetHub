class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_list = defaultdict(list)
        prev = [float('inf')] * n
        prev[src] = 0

        for from_city, to_city, price in flights:
            adj_list[to_city].append((from_city, price))


        for i in range(k + 1):
            cur = [float(inf)] * n
            cur[src] = 0
            for to_city in range(n):
                for from_city, price in adj_list[to_city]:
                    expected_price = price + prev[from_city]
                    cur[to_city] = min(cur[to_city], expected_price)
        
            prev = copy.deepcopy(cur)
        return -1 if prev[dst] == float('inf') else prev[dst]


