class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curTime = 0
        queue = deque()
        totalTime = 0
        
        for customer in customers:
            queue.append(customer)
            
        while queue:
            customer = queue.popleft()
            curTime = max(curTime, customer[0])
            totalTime += (curTime + customer[1] - customer[0])    
            curTime += customer[1]
        
        return totalTime / len(customers)
        