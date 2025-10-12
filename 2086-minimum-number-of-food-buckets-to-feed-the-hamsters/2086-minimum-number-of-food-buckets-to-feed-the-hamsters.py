class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        '''
        Time: O(n)
        Space: O(1)

        '''

        n = len(hamsters)
        num_buckets = 0
        i = 0

        while i < n:
            val = hamsters[i]

            if val == 'H':
                if (i == 0 or hamsters[i - 1] == 'H') and (i == n - 1 or hamsters[i + 1] == 'H'):
                    return -1
                num_buckets += 1
                if i + 1 < n and hamsters[i + 1] == '.':
                    # if possible, putting a bucket on the right is always the better choice
                    i += 3
                else:
                    i += 1
            else:
                i += 1

        return num_buckets