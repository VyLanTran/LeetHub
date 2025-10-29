class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # min_price = float('inf')
        queue = deque([(src, 0)])
        stops = 0
        adj_list = defaultdict(list)
        prices = [float('inf')] * n
        prices[src] = 0

        for from_city, to_city, price in flights:
            adj_list[from_city].append((to_city, price))

        while stops <= k and queue: 
            size = len(queue)
            for _ in range(size):
                city, price = queue.popleft()
              
                for next_city, next_price in adj_list[city]:
                    expected_price = price + next_price
                    if prices[next_city] > expected_price:
                        queue.append((next_city, price + next_price))
                        prices[next_city] = expected_price
            stops += 1
           

        return -1 if prices[dst] == float('inf') else prices[dst]