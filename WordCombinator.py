import random
from multiprocessing import process

possible_words = []
# variable to change words per line inside the txt file
words_per_line = 10

def write_random_words():

    # read the file and store words in the list
    try:
        with open('Words.txt', 'r') as word_stream:
            # loop through the lines and strip ansii codes
            for line in word_stream:
                cleaned_line = line.rstrip('\r\n')
                # appemd cleaned lines to the list
                possible_words.append(cleaned_line)

    except OSError:
        return

    # write 100 random words from the list into the combined words file
    try:
        with open("CombinedWords.txt", 'w') as combined_words:

            for i in range (100):
                random_index = random.randrange(len(possible_words))
                random_word = possible_words[random_index]
                combined_words.write(f"{random_word} ")

                # checks if words per line is divisible by 'i' with remainder 0
                if (i+1) % words_per_line == 0:
                    combined_words.write("\n")
    except OSError:
        return

def remove_spaces():
    try:
        # open the combined words file
        with open("CombinedWords.txt", 'r') as combined_words:
            # assign lines to lines
            lines = combined_words.readlines()

        with open("Spaces_Removed.txt", 'w') as spaces_removed:
            # loop through each line and remove spaces
            for line in lines:
                cleaned_line = line.replace(" ","")
                # write to the spaces_removed file
                spaces_removed.write(cleaned_line)
    except OSError:
        return


while True:
    remove_space_input = input("Write a book? (y/n)")
    if remove_space_input == "y":
        write_random_words()
        break
    else:
        break

while True:
    remove_space_input = input("Remove Spaces? (y/n)")
    if remove_space_input == "y":
        remove_spaces()
        break
    else:
        break