class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr = [[arr[i], i] for i in range(len(arr))]
        arr.sort(key=lambda x:x[0])
        res = [0 for _ in range(len(arr))]
        rank, curVal = 0, float('-inf')
        for val, index in arr:
            if val > curVal:
                rank += 1
            res[index] = rank
            curVal = val
        return res