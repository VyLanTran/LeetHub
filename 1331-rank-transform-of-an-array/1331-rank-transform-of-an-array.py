class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        minHeap = copy.deepcopy(arr)
        heapify(minHeap)
        valToRank, rank, curVal = {}, 0, float('-inf')
        while minHeap:
            val = heappop(minHeap)
            if val > curVal:
                rank += 1
            valToRank[val] = rank
            curVal = val
        arr = [valToRank[val] for val in arr]
        return arr
        
            