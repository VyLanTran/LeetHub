class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        set1 = set(nums1) then
            - take all if len(set1) <= len(nums1) / 2
            - else only take the most "optimal" len(nums1) / 2 elements
        {1, 2, 3, 4, 5, 6} -> only take 3
        {3, 4, 8, 9, 10, 11}
        
        prioritize the smaller set
        
        take intersection of set1, set2
        
        '''
        
        # a = {1, 2, 3, 4}
        # b = {1, 4 }
        # print(a-b)
        
        n = len(nums1)
        set1, set2 = set(nums1), set(nums2)
        
        print(set1, set2)
        
        if len(set1) <= n // 2 and len(set2) <= n // 2:
            return len(set1 | set2)
        if len(set1) <= n // 2:
            inter = set1 & set2
            comp = set2 - inter
            return len(set1) + min(n // 2, len(comp))
        if len(set2) <= n // 2:
            '''
            inter = {2, 3}
            comp = {1, 4, 5, 6}
            
            {2, 3}
            '''
            inter = set1 & set2
            comp = set1 - inter
            return len(set2) + min(n // 2, len(comp))
        
        
        '''
        inter = {2, 4}
        comp1 = {1}
        comp2 = {10}
        1, 10 + max(2-1, 2-1)
        '''
        inter = set1 & set2
        comp1, comp2 = set1 - inter, set2 - inter
        if len(comp1) >= n // 2 and len(comp2) >= n // 2:
            return n
        if len(comp1) < n // 2 and len(comp2) < n // 2:
            return len(comp1) + len(comp2) + min(len(inter), n-len(comp1)-len(comp2))
        return n
        
            
                