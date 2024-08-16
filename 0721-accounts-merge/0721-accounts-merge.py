class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        numAccounts = len(accounts)
        visitedAccounts = [False for _ in range(numAccounts)]
        emailAccountMap = dict()
        res = []

        def buildGraph():
            for id, account in enumerate(accounts):
                for i in range(1, len(account)):
                    email = account[i]
                    if email not in emailAccountMap:
                        emailAccountMap[email] = []
                    emailAccountMap[email].append(id)
                    
        buildGraph()
        
        def dfs(id, emails):
            if visitedAccounts[id]:
                return
            visitedAccounts[id] = True
            for i in range(1, len(accounts[id])):
                email = accounts[id][i]
                emails.add(email)
                if email in emailAccountMap:
                    for id2 in emailAccountMap[email]:
                        dfs(id2, emails)
        
        for id, account in enumerate(accounts):
            if visitedAccounts[id]:
                continue
            # print(id)
            emails = set()
            name = account[0]
            dfs(id, emails)
            emails = list(emails)
            emails.sort()
            # print(emails)
            arr = [name]
            arr.extend(emails)
            res.append(arr)
        
        return res
            


        '''
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
        '''
            
            
            