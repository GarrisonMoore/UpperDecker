from logging import NullHandler

possible_words = []

combined_words = open("CombinedWords.txt", 'w')


def readFile():
    try:
        word_stream = open('Words.txt', 'r')

        line = word_stream.readline()

        while line is not None:
            line = word_stream.readline()
            possible_words.append(f"{line} ")
    except:
        raise TypeError


readFile()
print(possible_words)