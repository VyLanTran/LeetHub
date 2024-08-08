class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.lead = None
    
    def findLead(self, persons):
        freq = dict()
        lead = dict()
        maxVotes = 0
        lastLead = 0
        for i in range(len(persons)):
            person = persons[i]
            freq[person] = freq.get(person, 0) + 1
            if freq[person] >= maxVotes:
                maxVotes = freq[person]
                lastLead = person
                lead[i] = person
            else:
                lead[i] = lastLead
        self.lead = lead

    def q(self, t: int) -> int:
        if not self.lead:
            self.findLead(self.persons)
        i = self.binSearch(self.times, t)
        # return self.findWinner(i)
        return self.lead[i] 
    
    def binSearch(self, arr, t):
        # find the largest index st arr[index] <= t
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = arr[mid]
            if val == t:
                return mid
            elif val > t:
                right = mid - 1
            else:
                if mid == len(arr) - 1 or arr[mid + 1] > t:
                    return mid
                left = mid + 1
        return left
    
#     def findWinner(self, index):
#         map = dict()
#         maxVotes = 0
#         res = 0
#         for i in range(index + 1):
#             person = self.persons[i]
#             map[person] = map.get(person, 0) + 1
#             if map[person] >= maxVotes:
#                 maxVotes = map[person]
#                 res = person
#         return res
        
            


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)