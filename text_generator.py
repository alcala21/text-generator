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
        self.map = defaultdict(dict)
        self.res = []
        self.starters = []

    def tokenize(self):
        self.tokens = Tokenizer.tokenize(self.text)

    def build_bigrams(self):
        self.bigrams = [(self.tokens[i], self.tokens[i + 1]) for i in range(len(self.tokens) - 1)]

    def summarize_bigrams(self):
        for bi in self.bigrams:
            self.map[bi[0]][bi[1]] = self.map[bi[0]].get(bi[1], 0) + 1

        self.starters = [x for x, v in self.map.items()
                        if self.starter(x) and len(v) > 2]

    @staticmethod
    def starter(word):
        return bool(re.match(r"^[A-Z][^.!?]*[a-z,]?$", word))

    @staticmethod
    def middle(word):
        return bool(re.match(r".*[a-z,]$", word))

    @staticmethod
    def ending(word):
        return bool(re.match(r".*[\.!\?]$", word))

    @staticmethod
    def sample_word(words, values):
        return random.choices(population=words, weights=values,k=1)[0]

    def generate_sentence(self):
        if not self.res:
            self.res = [random.choice(self.starters)]

        if len(self.res) >= 5 and self.ending(self.res[-1]):
            return None

        wl = self.map[self.res[-1]]

        word = self.sample_word(list(wl.keys()), list(wl.values()))

        if self.middle(word):
            self.res += [word]
        elif self.ending(word) and len(self.res) >= 5:
            self.res += [word]
        else:
            self.res.pop(-1)

        self.generate_sentence()

    def generate_sentences(self):
        for i in range(10):
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

