# Write your code here
import random
from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict
import re
Tokenizer = WhitespaceTokenizer()


class TextGenerator:

    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.bigrams = []
        self.all_tokens = 0
        self.unique_tokens = 0
        self.res = []

    def tokenize(self):
        self.tokens = Tokenizer.tokenize(self.text)

    def build_bigrams(self):
        self.bigrams = [(self.tokens[i], self.tokens[i + 1]) for i in range(len(self.tokens) - 1)]

    def summarize_bigrams(self):
        temp = defaultdict(dict)
        for bi in self.bigrams:
            temp[bi[0]][bi[1]] = temp[bi[0]].get(bi[1], 0) + 1

        self.bigrams = dict([(k, dict(sorted(v.items(), reverse=True, key=lambda x: x[1]))) for k, v in temp.items()])
        temp = None

    def generate_word(self, pos="first", wl=dict()):
        word = ""
        words = list(wl.keys())
        values = list(wl.values())
        count = 0

        if pos == "first":
            all_words = list(self.bigrams.keys())
            while not re.match(r"^[A-Z].*[a-z,]$", word):
                word = random.choice(all_words)
        elif pos == "middle":
            while not re.match(r".*[a-z,]$", word) and count < len(words):
                word = random.choices(population=words, weights=values, k=1)[0]
                count += 1
        elif pos == "end":
            while not re.match(r".*[\.!\?]$", word) and count < len(words):
                word = words[count]
                count += 1

        if count == len(words) and pos != "first":
            return None
        return word

    def generate_sentence(self):
        if not self.res:
            self.res = [self.generate_word()]

        if len(self.res) >= 5:
            if re.match(r".*[\.!\?]$", self.res[-1]):
                return None

        wl = self.bigrams[self.res[-1]]

        if 0 < len(self.res) < 5:
            word = self.generate_word("middle", wl)
            if not word:
                self.res = self.res[:-1]
                return self.generate_sentence()
            else:
                self.res += [word]
        else:
            word = self.generate_word("end", wl)
            if not word:
                self.res += [random.choice(list(wl.keys()))]
                return self.generate_sentence()
            else:
                self.res += [word]
                return None

        return self.generate_sentence()

    def generate_sentences(self):
        for _ in range(10):
            self.res = []
            self.generate_sentence()
            print(" ".join(self.res))


def start():
    file = input()
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    tg = TextGenerator(text)
    tg.tokenize()
    tg.build_bigrams()
    tg.summarize_bigrams()
    tg.generate_sentences()


if __name__ == "__main__":
    start()

