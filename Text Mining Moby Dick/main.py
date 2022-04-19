import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import sent_tokenize, word_tokenize, pos_tag, FreqDist
import matplotlib.pyplot as plt
import re

TOP_FREQ = 20


class BookLoader:
    def __init__(self, path):
        self._txt_book = open(path, encoding="utf8").read()
        self._sentences = None
        self._tokens = None

    def get_txt_book(self):
        return self._txt_book

    def get_sentences(self):
        if self._sentences is None:
            self._sentences = sent_tokenize(self._txt_book)
        return self._sentences

    def get_tokens(self, is_lower: bool, is_alpha: bool):
        if self._tokens is None:
            self._tokens = word_tokenize(self._txt_book)
        if is_lower and is_alpha:
            return [token.lower() for token in self._tokens if token.isalpha()]
        elif is_lower:
            return [token.lower() for token in self._tokens]
        elif is_alpha:
            return [token for token in self._tokens if token.isalpha()]
        return self._tokens


def plot_freq(tokens, title):
    freq_tokens = FreqDist(tokens)
    sorted_tokens = sorted(freq_tokens.values(), reverse=True)

    plt.title(title)
    plt.xlabel("log rank")
    plt.ylabel("log frequency")
    plt.loglog(range(len(sorted_tokens)), sorted_tokens)
    plt.grid()
    plt.show()
    print(freq_tokens.most_common(TOP_FREQ))  # most 20 common words in book


def question4b(data_loader: BookLoader):
    tokens = data_loader.get_tokens(True, True)
    plot_freq(tokens, "Tokens occurrences")


def question4c(data_loader: BookLoader):
    tokens = data_loader.get_tokens(True, True)
    stop_words = set(stopwords.words('english'))
    tokens_without_stop_words = [word for word in tokens if word not in stop_words]
    plot_freq(tokens_without_stop_words, "Tokens without stop words occurrences")


def question4d(data_loader: BookLoader):
    tokens = data_loader.get_tokens(True, True)
    stop_words = set(stopwords.words('english'))
    porter_stemmer = PorterStemmer()
    tokens_without_stop_words_with_stem = [porter_stemmer.stem(word) for word in tokens if word not in stop_words]
    plot_freq(tokens_without_stop_words_with_stem, "Tokens without stop words with stem occurrences")


def question4e(data_loader: BookLoader):
    word_tokens = data_loader.get_tokens(False, False)
    position_tokens = pos_tag(word_tokens)

    grammar = "adjectives_and_nouns: {<JJ|JJS|JJR>+<NNS|NNP|NNPS|NN>+}"
    text_regex = nltk.RegexpParser(grammar)
    parse_text = text_regex.parse(position_tokens)

    parse_lst = []
    for node in parse_text:
        if isinstance(node, nltk.tree.Tree) and node.label() == 'adjectives_and_nouns':
            parse_lst.append(" ".join([leaf[0] for leaf in node.leaves()]))
    plot_freq(parse_lst, "POS-tagging occurrences")


def question4f(data_loader: BookLoader):
    word_tokens = data_loader.get_tokens(False, True)
    position_tokens = pos_tag(word_tokens)
    print(position_tokens)


def question4g(data_loader: BookLoader):
    raw_text = data_loader.get_txt_book()
    word_tokens = [token.lower() for token in word_tokenize(raw_text)]
    pos_lower_tokens = pos_tag(word_tokens)  # tuple
    d_count = dict()
    for pos in pos_lower_tokens:
        if pos not in d_count.keys():
            d_count[pos] = 0
        d_count[pos] = d_count[pos] + 1

    sort_lst = list(sorted(d_count.items(), key=lambda item: item[1]))
    top_ten_occur = sort_lst[-10:]
    print("print the top ten of occurrences in book:")
    for i in top_ten_occur:
        print(i)

    print("")

    print("print the less ten of occurrences in book:")
    less_ten_occur = sort_lst[:10]
    for i in less_ten_occur:
        print(i)


def question4h(data_loader: BookLoader):
    word_tokens = data_loader.get_tokens(False, False)
    pos_lower_tokens = pos_tag(word_tokens)  # tuple

    lst = [word[0] for word in pos_lower_tokens if word[1] in ["NNP", "NNPS"]]
    textfile = open("a_file.txt", "w", encoding="utf8")

    for element in lst:
        textfile.write(element + "\n")


def question4i(data_loader: BookLoader):
    raw_text = data_loader.get_txt_book()
    punctuation_sep = ',\\.-?:_!'
    regex = f"\\b([^\\s]+)[{punctuation_sep}]?(\\s+\\1\\b)"
    couples_of_words = re.findall(regex, raw_text)
    for i in couples_of_words:
        print(f"{i[0]} {i[1]}")





if __name__ == '__main__':
    #nltk.download('stopwords')
    nltk.download('averaged_perceptron_tagger')
    data_loader = BookLoader(r"Mobi_Dick.txt")
    #question4b(data_loader)
    #question4c(data_loader)
    #question4d(data_loader)
    question4e(data_loader)
    #question4f(data_loader)
    #question4g(data_loader)
    #question4g(data_loader)
    #question4i(data_loader)



