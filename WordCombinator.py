import random
from logging import NullHandler

possible_words = []

def readFile():
    """Internal method for the write_random_words method"""
    try:
        with open('Words.txt', 'r') as word_stream:

            for line in word_stream:
                cleaned_line = line.rstrip('\r\n')
                possible_words.append(cleaned_line)

    except OSError:
        return



def write_random_words():

    readFile()

    words_per_line = 10

    try:
        with open("CombinedWords.txt", 'w') as combined_words:

            for i in range (100):
                random_index = random.randrange(len(possible_words))
                random_word = possible_words[random_index]

                combined_words.write(f"{random_word} ")

                if (i+1) % words_per_line == 0:
                    combined_words.write("\n")
    except OSError:
        return

write_random_words()

def remove_spaces():
    try:
        with open("CombinedWords.txt", 'r') as combined_words:
            lines = combined_words.readlines()

        with open("CombinedWords.txt", 'w') as combined_words:
            for line in lines:

                cleaned_line = line.rstrip(" \n")
                combined_words.write(cleaned_line + "\n")

    except OSError:
        return

remove_spaces()

