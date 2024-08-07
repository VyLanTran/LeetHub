class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(' ')
        arr = [(len(words[i]), i, words[i].lower()) for i in range(len(words))]
        arr.sort(key=lambda x:[x[0], x[1]])
        # print(arr)
        res = ""
        for i in range(len(arr)):
            word = arr[i][2]
            if i == 0:
                res += word[0].upper() + word[1:] + " "
            elif i == len(arr) - 1:
                res += word
            else:
                res += word + " "
        return res
            
                
