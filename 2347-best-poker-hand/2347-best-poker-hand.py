class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        '''
        Time: O(1)
        Space: O(1)
        '''
        if len(set(suits)) == 1:
            return "Flush"
        
        counter = Counter(ranks)
        max_freq = max(counter.values())

        if max_freq >= 3:
            return "Three of a Kind"
        if max_freq == 2:
            return "Pair"
        return "High Card"