class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        '''
        Time: O(n)
        Space: O(1)
        '''

        num_bulls = 0
        secret_freq, guess_freq = defaultdict(int), defaultdict(int)

        for i in range(len(secret)):
            a, b = secret[i], guess[i]
            if a == b:
                num_bulls += 1
            else:
                secret_freq[a] += 1
                guess_freq[b] += 1

        num_cows = sum(min(secret_freq[key], guess_freq[key]) for key in guess_freq)
        # return str(num_bulls) + "A" + str(num_cows) + "B"
        return "{}A{}B".format(num_bulls, num_cows)
     