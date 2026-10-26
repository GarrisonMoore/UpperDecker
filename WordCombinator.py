"""Edited 9/27/2026 - Garrison Moore

This program will use either
    * User-defined input file
    * Or default to a list of all possible english words (Words.txt)

The program will:
    * Scramble the words from that file and produce a new 'ScrambledWords.txt' file
    * Remove spaces from that file if the user wants"""


import random

# a list to store all possible words. Used to select a random index / word later
possible_words = []
# variable to change words per line inside the txt file
words_per_line = 10

def write_random_words():
    """Method reads Words.txt which contains almost all english words in existence, writes words in random order to a file."""
    # read the file and store words in the list
    while True:
        input_file = input("Define a file to scramble or \npress enter to use random words\n: ")
        # if user presses 'enter' then default to Words.txt
        if input_file == "":
            input_file = "Words.txt"
        # try to open defined file
        try:
            with open(input_file, 'r') as word_stream:
                # loop through the lines and strip ansi codes
                for line in word_stream:
                    cleaned_line = line.rstrip('\r\n')
                    # append cleaned lines to the list
                    possible_words.append(cleaned_line)
            break  # Exit the loop once the file is successfully read
        # print error for invalid input
        except OSError:
            print(f"\nFile '{input_file}' not found. Please try again.\n")

    # write 100 random words from the list into the ScrambledWords.txt file
    try:
        with open("ScrambledWords.txt", 'w') as output_file:
            word_length = len(possible_words)

            for i in range (word_length):
                random_index = random.randrange(len(possible_words))
                random_word = possible_words[random_index]
                output_file.write(f"{random_word} ")

                # checks if words per line is divisible by 'i' with remainder 0
                if (i+1) % words_per_line == 0:
                    output_file.write("\n")

        print("\nCheck 'ScrambledWords.txt'")
    except OSError:
        print("Write failed.")
        return

def remove_spaces():
    """Method removes spaces from the ScrambledWords.txt file"""
    try:
        # open the combined words file in read mode
        with open("ScrambledWords.txt", 'r') as combined_words:
            # assign lines to lines
            lines = combined_words.readlines()
        # open the CombinedWords.txt file in write mode
        with open("ScrambledWords.txt", 'w') as spaces_removed:
            # loop through each line and remove spaces
            for line in lines:
                cleaned_line = line.replace(" ","")
                # write to the spaces_removed file
                spaces_removed.write(cleaned_line)
    except OSError:
        print("Removing spaces failed.")
        return

# Terminal loop
write_random_words()

while True:
    remove_space_input = input("Remove Spaces? (y/n) \n:")
    if remove_space_input.lower() == "y":
        remove_spaces()
        break
    elif remove_space_input.lower() == "n":
        break
    else:
        print(f"Invalid input '{remove_space_input}'. Try again.")