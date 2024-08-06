class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = dict()
        for c in word:
            freq[c] = freq.get(c, 0) + 1
        arr = [val for val in freq.values()]
        arr.sort(reverse = True)
        i, res = 0, 0
        while i < len(arr):
            if i < 8:
                res += arr[i]
            elif i < 16:
                res += 2 * arr[i]
            elif i < 24:
                res += 3 * arr[i]
            else:
                res += 4 * arr[i]
            i += 1
        return res