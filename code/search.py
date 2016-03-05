# This program let a user search for a word.
# It will show a word, its origin, and its difficulty level.
# Currently there are two attributes for each word: origin and difficulty.
#
# Origin (given)
# 
# 1: Arabic
# 2: Asian
# 3: Dutch
# 4: Eponyms
# 5: French
# 6: German
# 7: Greek
# 8: Italian
# 9: Japanese
# 10: Latin
# 11: New World
# 12: Old English
# 13: Slavic
# 14: Spanish
#
# Difficulty (A user can change the difficulty. For normal words, it is either
#               1 or 2 (default), while for challenging words, it is either 3
#               or 4 (default).)
#   0: all
#   1: easy
#   2: hard (default)
#   3: challenging-easy
#   4: challenging-hard (default)
#

import sys
import pandas as pd

# Numbers of origins & difficulties are given.
num_origins = 14
origins_all = ["Arabic", "Asian", "Dutch", "Eponyms", "French", "German",
    "Greek", "Italian", "Japanese", "Latin", "New World", "Old English",
    "Slavic", "Spanish"]
num_difficulties = 4

# Filename for words (in csv, format: word, origin, difficulty, with header)
word_filename = '../data/words.csv'

def get_input():
    """
    Obtain the user input
    """
    word = ""
    print "----------------------------------------------------------"
    input_str = raw_input("Enter a word (q for quit): ")
    print "----------------------------------------------------------"
    words = input_str.split()
    if len(words) != 0: # Only the first one will be searched.
        word = words[0] 
    return word

# Read word file.
def read_words(word_filename):
    """
    Reads the word file in csv format, and returns the pandas data frame.
    """
    df = pd.read_csv(word_filename)
    df.set_index('word', inplace=True)
    return df

def main():
    """
    main fucntion
    """
    # Read word data.
    df = read_words(word_filename)

    print "Origin of words."
    print "   0: all (default)"
    for i in range(num_origins):
        print "   " + str(i + 1) + ": " + origins_all[i]
    print
    print "Difficulty of words."
    print "   0: all (default)"
    print "   1: easy"
    print "   2: hard"
    print "   3: challenging-easy"
    print "   4: challenging-hard"

    word = ""

    # Get user inputs for a word
    while True:
        word = get_input()
        if word == "":
            continue
        if word == "q":
            break
        # Finds a word
        try:
            row = df.loc[word]
            origin = row['origin']
            difficulty = row['difficulty']
            print "Word: " + word + " (Origin: " + origins_all[origin] + \
                ", Difficulty: " + str(difficulty) + ")"
        except KeyError:
            print "# The word does not exist in the list. Try again."
    

if __name__ == "__main__":
    main()
