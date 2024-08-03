class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        '''
        b: a means a rabbits said b other rabbits having same color
        
        - if a == b ==> that type of color has b + 1 rabbits
        - if a < b ==> that type has b + 1 rabbits
        - if a > b
            group_size = b + 1
            group_num = a // group_size + 1   (1 more group is from a % group_size + some extra) rabbits
            rabbit_num = group_num * group_size
                       = (a // (b + 1) + 1) * (b + 1)
        
        2 rabbits said 1 other rabbit same color
        
        '''
        map = dict()
        res = 0
        for answer in answers:
            map[answer] = map.get(answer, 0) + 1
        for b, a in map.items():
            if a == b or a < b:
                res += (b + 1)
            else:
                groupSize = b + 1
                groupNum = a // groupSize if a % groupSize == 0 else a // groupSize + 1
                res += groupNum * groupSize
        return res
        