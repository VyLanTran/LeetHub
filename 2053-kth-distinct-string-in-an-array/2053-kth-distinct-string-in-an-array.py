class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        '''
        visited : d, b, c, a
        dup     : b, c
        queue   : 
        '''
        
        visited, duplicate = set(), set()
        for s in arr:
            if s in visited:
                duplicate.add(s)
            visited.add(s)
        counter = 0
        for s in arr:
            if s not in duplicate:
                counter += 1
                if counter == k:
                    return s
        return ""
        
        
                