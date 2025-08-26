class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr)
        res = 0

        def count_ways(tup):
            tup_counter = Counter(tup)
            res = 1
            for num, count in tup_counter.items():
                res *= comb(counter[num], count) 
            return res

        arr.sort()
        arr_len = len(arr)

        for i in range(arr_len - 2):
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            j, k = i + 1, arr_len - 1
            while j < k:
                if j > i + 1 and arr[j] == arr[j - 1]:
                    j += 1
                elif k < arr_len - 1 and arr[k] == arr[k + 1]:
                    k -= 1
                else:
                    three_sum = arr[i] + arr[j] + arr[k] 
                    if three_sum == target:
                        res += count_ways((arr[i], arr[j], arr[k]))
                        res %= (10**9 + 7)
                        j += 1
                        k -= 1
                    elif three_sum < target:
                        j += 1
                    else:
                        k -= 1


        return res


        

