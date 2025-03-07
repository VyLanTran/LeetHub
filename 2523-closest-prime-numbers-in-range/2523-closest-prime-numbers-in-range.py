class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True] * (right + 1)
        isPrime[0] = False
        isPrime[1] = False
        
        for i in range(2, right + 1):
            if isPrime[i]:
                for j in range(2*i, right + 1, i):
                    isPrime[j] = False

        prime1, prime2 = -1, right
        prev = None

        for i in range(left, right + 1):
            if isPrime[i]:
                if prev is not None and i - prev < prime2 - prime1:
                    prime1, prime2 = prev, i
                prev = i

        return [prime1, prime2] if prime1 != -1 else [-1, -1]
