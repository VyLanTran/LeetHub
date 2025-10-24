class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        a -> [[a]]
        aa -> [[a, a], [aa]]
        aab
            # every single ways for s[:i-1] (just add b as the last substring into each substring)
            is there any palindrome ending with s[i]?
                for j from 0 to i
                    if s[j:i] is a palindrome, then reuse all the elements from f(j-1)

      
        '''

        def is_palindrome(left, right):
            while left <= right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        dp = {}

        def f(i):
            if i < 0:
                return [[]]
            if i == 0:
                return [[str(s[0])]]
            if i in dp:
                return dp[i]
            res = []
            for j in range(i + 1):
                if is_palindrome(j, i):
                    palindrome = s[j:(i + 1)]
                    prev_partitions = copy.deepcopy(f(j - 1))
                    # print(f'cur pal={palindrome}, prev_par = {prev_partitions}')
                    # prev_partitions = f(j - 1)
                    for partition in prev_partitions:
                        partition.append(palindrome)
                    res.extend(prev_partitions)
            dp[i] = res
            return res

        res = f(len(s) - 1)
        # print(dp)
        # print(f'is pal: {is_palindrome(0, 2)}')
        return res

        '''
        012
        aab

        f(2)
            res = []
            j: 1 to 2

        '''