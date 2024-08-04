class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # n = len(deck)

        # def pattern(n):
        #     arr = deque([i for i in range(n)])
        #     res = []
        #     while arr:
        #         if len(arr) == 1:
        #             res.append(arr.popleft())
        #             break
        #         res.append(arr.popleft())
        #         arr.append(arr.popleft())
        #     return res
        
        # order = pattern(n)
        # deck.sort()
        # pairs = [(order[i], deck[i]) for i in range(n)]
        # pairs.sort(key=lambda x:x[0])
        # res = [pair[1] for pair in pairs]
        # return res

        n = len(deck)
        res = [0 for _ in range(n)]
        queue = deque([i for i in range(n)])
        deck.sort()

        for i in range(n):
            index = queue.popleft()
            if i < n - 1:
                queue.append(queue.popleft())
            res[index] = deck[i]

        return res

