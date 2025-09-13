class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def insert_spaces(num_spaces):
            return " " * num_spaces

        def format(included_words, is_last_line):
            if is_last_line:
                sentence = " ".join(included_words)
                sentence += insert_spaces(maxWidth - len(sentence))
                return sentence

            if len(included_words) == 1:
                return included_words[0] + insert_spaces(maxWidth - len(included_words[0]))

            num_slots = len(included_words) - 1
            num_spaces = maxWidth - sum(len(word) for word in included_words) 
            extra_slots = num_spaces % num_slots
            sentence = ""

            for i, word in enumerate(included_words):
                if i == len(included_words) - 1:
                    sentence += word
                elif i < extra_slots:
                    sentence += word + insert_spaces(ceil(num_spaces / num_slots))
                else:
                    sentence += word + insert_spaces(floor(num_spaces / num_slots))
            
            return sentence


        i  = 0
        res = []

        while i < len(words):
            cur_len = 0
            included_words = []

            while i < len(words):
                expected_len = cur_len + len(words[i]) + (1 if cur_len > 0 else 0)
                if expected_len <= maxWidth:
                    included_words.append(words[i])
                    cur_len = expected_len 
                    i += 1
                else:
                    break
            
            if i == len(words):
                res.append(format(included_words, True))
            else:
                res.append(format(included_words, False))

        return res