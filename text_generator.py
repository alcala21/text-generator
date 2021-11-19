# Write your code here
from nltk.tokenize import WhitespaceTokenizer
Tokenizer = WhitespaceTokenizer()


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

    def print_bigram_stats(self):
        print("Number of bigrams:", len(self.bigrams))

    def print_bigram(self, i):
        print(f"Head: {self.bigrams[i][0]}    Tail: {self.bigrams[i][1]}")

    def get_bigram(self):
        print()
        while True:
            try:
                val = input()
                if val == "exit":
                    break
                val = int(val)
                self.print_bigram(val)
            except ValueError:
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input a value that is not greater than the number of all bigrams.")


def start():
    file = input()
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    tg = TextGenerator(text)
    tg.tokenize()
    tg.build_bigrams()
    tg.print_bigram_stats()
    tg.get_bigram()


if __name__ == "__main__":
    start()
