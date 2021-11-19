# Write your code here
from nltk.tokenize import WhitespaceTokenizer
Tokenizer = WhitespaceTokenizer()
from collections import defaultdict


class TextGenerator:

    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.bigrams = []
        self.all_tokens = 0
        self.unique_tokens = 0

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

    def print_tails(self, _val):
        print(f"Head: {_val}")
        td = self.bigrams[_val]
        for k, v in td.items():
            print(f"Tail: {k:10s}    Count: {v}")

    def get_bigram(self):
        while True:
            print()
            try:
                val = input()
                if val == "exit":
                    break
                self.print_tails(val)
            except ValueError:
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input a value that is not greater than the number of all bigrams.")
            except KeyError:
                print("Key Error. The requested word is not in the model. Please input another word.")


def start():
    file = input()
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    tg = TextGenerator(text)
    tg.tokenize()
    tg.build_bigrams()
    tg.summarize_bigrams()
    tg.get_bigram()


if __name__ == "__main__":
    start()
