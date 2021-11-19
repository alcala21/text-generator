# Write your code here
from nltk.tokenize import WhitespaceTokenizer
Tokenizer = WhitespaceTokenizer()


class TextGenerator:

    def __init__(self, text):
        self.text = text
        self.tokens = []
        self.all_tokens = 0
        self.unique_tokens = 0

    def tokenize(self):
        self.tokens = Tokenizer.tokenize(self.text)

    def print_stats(self):
        self.all_tokens = len(self.tokens)
        self.unique_tokens = len(set(self.tokens))
        print("Corpus statistics")
        print("All tokens:", self.all_tokens)
        print("Unique tokens:", self.unique_tokens)

    def get_token(self):
        print()
        while True:
            try:
                val = input()
                if val == "exit":
                    break
                val = int(val)
                print(self.tokens[val])
            except ValueError:
                print("Type Error. Please input an integer.")
            except IndexError:
                print("Index Error. Please input an integer that is in the range of the corpus.")


def start():
    file = input()
    # file = "corpus.txt"
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    tg = TextGenerator(text)
    tg.tokenize()
    tg.print_stats()
    tg.get_token()


if __name__ == "__main__":
    start()


