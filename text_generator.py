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
    def middle(word):
        return bool(re.match(r".*[A-z,]$", word))

    @staticmethod
    def ending(word):
        return bool(re.match(r".*[\.!\?]$", word))

    @staticmethod
    def sample_word(words, values):
        return random.choices(population=words, weights=values,k=1)[0]

    def generate_sentence(self):
        count = 0
        while True:
            if not self.res:
                self.res = random.choice(self.starters).split()

            if len(self.res) >= 5 and self.ending(self.res[-1]):
                break

            self.add_words()
            count += 1
            if count == 100:
                a = 1

    def add_words(self):
        key = " ".join(self.res[-2:])
        wl = self.map[key]
        if len(wl) == 0:
            bkey = " ".join(self.res[-3:-1])
            self.map[bkey].pop(self.res.pop(-1))
            return
        word = self.sample_word(list(wl.keys()), list(wl.values()))

        if self.middle(word):
            self.res += [word]
        elif self.ending(word) and len(self.res) >= 4:
            self.res += [word]
        else:
            if len(self.res) > 2:
                self.res.pop(-1)
                self.map[key].pop(word)
            else:
                self.res = []

    def generate_sentences(self):
        for i in range(10):
            self.res = []
            self.generate_sentence()
            print(" ".join(self.res))


def start():
    # file = input()
    file = "corpus.txt"
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    tg = TextGenerator(text)
    tg.tokenize()
    tg.build_trigrams()
    tg.summarize_trigrams()
    tg.generate_sentences()


if __name__ == "__main__":
    start()
    
