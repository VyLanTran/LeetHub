class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def createGraph():
            graph = dict()
            emailToName = dict()
            
            for account in accounts:
                name = account[0]
                for i in range(1, len(account)):
                    email = account[i]
                    emailToName[email] = name
                    if email not in graph:
                        graph[email] = set()
                    
                    for j in range(1, len(account)):
                        if j != i:
                            email2 = account[j]
                            if email2 not in graph:
                                graph[email2] = set()
                            graph[email].add(email2)
                            graph[email2].add(email)
                    
            
            return graph, emailToName
        
        graph, emailToName = createGraph()
        visited = set()
        res = []
        temp = set()
        
        def dfs(email):
            temp.add(email)
            if email not in graph:
                return
            for email2 in graph[email]:
                if email2 in visited:
                    continue
                visited.add(email2)
                dfs(email2)
        
        
        for email in graph:
            if email in visited:
                continue
            temp = set()
            visited.add(email)
            dfs(email)
            arr = [emailToName[email]]
            emails = list(temp)
            emails.sort()
            arr.extend(emails)
            res.append(arr)
            
        return res
            
            
            