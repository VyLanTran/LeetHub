class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        self.graph = {kingName:[]}
        self.deathSet = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.graph:
            self.graph[parentName] = []
        self.graph[parentName].append(childName)
        

    def death(self, name: str) -> None:
        self.deathSet.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []            
        
        def dfs(name):
            nonlocal res
            if name not in self.deathSet:
                res.append(name)
            if name in self.graph:
                for child in self.graph[name]:
                    dfs(child)
                
        dfs(self.kingName)
        return res
    
    


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()