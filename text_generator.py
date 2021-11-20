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
        self.trigrams = []
        self.map = defaultdict(dict)
        self.res = []
        self.starters = []

    def tokenize(self):
        self.tokens = Tokenizer.tokenize(self.text)

    def build_trigrams(self):
        self.trigrams = [(self.tokens[i], self.tokens[i + 1], self.tokens[i + 2]) for i in range(len(self.tokens) - 2)]

    def summarize_trigrams(self):
        for tri in self.trigrams:
            self.map[" ".join(tri[:2])][tri[2]] = self.map[" ".join(tri[:2])].get(tri[2], 0) + 1

        self.starters = [x for x, v in self.map.items()
                        if self.starter(x) and len(v) > 2]

    @staticmethod
    def starter(word):
        return bool(re.match(r"^[A-Z][^.!?]*[a-z,]?$", word))

    @staticmethod
    def ending(word):
        return bool(re.match(r".*[\.!\?]$", word))

    @staticmethod
    def sample_word(words, values):
        return random.choices(population=words, weights=values,k=1)[0]

    def generate_sentence(self):
        if not self.res:
            self.res = random.choice(self.starters).split()

        if len(self.res) >= 5 and self.ending(self.res[-1]):
            return

        wl = self.map[" ".join(self.res[-2:])]
        self.res += [self.sample_word(list(wl.keys()), list(wl.values()))]

        return self.generate_sentence()

    def generate_sentences(self):
        for i in range(10):
            self.res = []
            self.generate_sentence()
            print(" ".join(self.res))


def start():
    file = input()
    # file = "corpus.txt"
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    tg = TextGenerator(text)
    tg.tokenize()
    tg.build_trigrams()
    tg.summarize_trigrams()
    tg.generate_sentences()


if __name__ == "__main__":
    start()
