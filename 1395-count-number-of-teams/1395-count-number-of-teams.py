class Solution:
    def numTeams(self, rating: List[int]) -> int:
        '''
        0 1 2 3 4
        2,5,3,4,1
        3 0 1 0 0     num elem larger than standing behind
        1 3 1 1 0
        
        increasing: 1 + 
        dec: 1 + 1
        '''
        n, res = len(rating), 0
        numSmaller = [0 for _ in range(n)]
        numLarger = [0 for _ in range(n)]
        
        for i in range(n):
            for j in range(i):
                if rating[j] > rating[i]:
                    numSmaller[j] += 1
                elif rating[j] < rating[i]:
                    numLarger[j] += 1
                    
        for i in range(n):
            j = i + 1
            while numLarger[i] > 0:
                if rating[j] > rating[i]:
                    res += numLarger[j]
                    numLarger[i] -= 1
                j += 1
                
        for i in range(n):
            j = i + 1
            while numSmaller[i] > 0:
                if rating[j] < rating[i]:
                    res += numSmaller[j]
                    numSmaller[i] -= 1
                j += 1
                
        return res
        
                     
        