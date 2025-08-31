class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        '''
        3,2,4,1

        after a flip arr[0:i], we get
            [i, i-1, i-2, ..., 1, 0, i+1, i+2, ..., n-1]
        we don't touch that last part (after i)
        so at each step, we aim to move that max element to the end
        ie, its correct position in the sorted arr, then don't touch
        that part any more

        3, 2, 4, 1
        -  -  -
        4, 2, 3, 1
        -  -  -  -
        1, 3, 2, 4
        -  -
        3, 1, 2, 4
        -  -  -
        2, 1, 3, 4
        -  -
        1, 2, 3, 4

        ===
        0 1 2 3 4  
        4 3 2 1 0
        '''

        n = len(arr)
        res = []

        def flip(start, end):
            i, j = start, end
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

        def find_max_index(start, end):
            max_num_index = start
            for i in range(start + 1, end + 1):
                if arr[i] > arr[max_num_index]:
                    max_num_index = i
            return max_num_index

        for i in range(n - 1, 0, -1):
            target = find_max_index(0, i)
            res.append(target + 1)
            flip(0, target)
            res.append(i + 1)
            flip(0, i)

        return res
