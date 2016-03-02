# This program randomly shows a group of words one by one.
# It should be used by a helper to quiz a spelling bee contestant.
# If a contestant got a word incorrect, the difficulty level will
# be updated.
#
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
import random

# For exception (will be used only for raising exception).
class RangeError(Exception):
    """
    User-defined exception for range errors.
    """
    pass

# Numbers of origins & difficulties are given.
num_origins = 14
origins_all = ["Arabic", "Asian", "Dutch", "Eponyms", "French", "German",
    "Greek", "Italian", "Japanese", "Latin", "New World", "Old English",
    "Slavic", "Spanish"]
num_difficulties = 4

# Maximum number for the quiz
max_num_words = 2000

# Filename for words (in csv, format: word, origin, difficulty, with header)
word_filename = '../data/words.csv'

def get_input():
    """
    Obtain the user input
    """
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

    print "Type a number, or a series of numbers separated by white spaces."

    origins_str = raw_input("Enter origins (default: all): ")
    difficulties_str = raw_input("Enter difficulties (default: all): ")
    num_words_str = raw_input("Enter the number of words (default: maximal): ")
    origins = origins_str.split()
    if len(origins) == 0: # no input, then the default value is assigned
        origins = ['0']
    difficulties = difficulties_str.split()
    if len(difficulties) == 0: # no input, then the default value is assigned
        difficulties = ['0']
    num_words = num_words_str.split()
    if len(num_words) == 0: # no input, then the default value is assigned
        num_words = ['max']  # 'max' represents maximal number.

    # Check if the input has only integers.
    try:
        origins2 = map(int, origins)
        for val in origins2:
            if val < 0 or val > num_origins:
                raise RangeError
        difficulties2 = map(int, difficulties)
        for val in difficulties2:
            if val < 0 or val > num_difficulties:
                raise RangeError
        num_words2 = (int(num_words[0]) if num_words[0] != 'max' \
                else max_num_words)
    except ValueError:
        print "# Bad input. Type integers separated by white spaces only."
        sys.exit()
    except RangeError:
        print "# Bad input: integers should be in range."
        print "             For origins, between 0 and", num_origins
        print "             For difficulties, between 0 and", num_difficulties
        sys.exit()
    # If origin=0 or difficulty=0, it should include all possibilities.
    if 0 in origins2:
        origins2 = range(1, num_origins + 1)
    if 0 in difficulties2:
        difficulties2 = range(1, num_difficulties + 1)
    
    return origins2, difficulties2, num_words2

# Read word file.
def read_words(word_filename):
    """
    Reads the word file in csv format, and returns the pandas data frame.
    """
    df = pd.read_csv(word_filename)
    df.set_index('word', inplace=True)
    return df

# Write word file.
def write_words(word_filename, df):
    """
    Writes the word file in csv format.
    """
    df.to_csv(word_filename)
    return

# Find words given the origin and the difficutly, and return them in a list.
def find_words(origin, difficulty, df):
    """
    Finds words given origin and difficulty
    """
    cond_origin = (df.origin == origin)
    cond_difficulty = (df.difficulty == difficulty)
    condition = cond_origin & cond_difficulty
    return df[condition].index.tolist()

def main():
    """
    main fucntion
    """
    # Read word data.
    df = read_words(word_filename)

    # Get user inputs for origins and difficulties
    origins, difficulties, num_words = get_input()
    print origins, difficulties, num_words

    # Find the list of words that satisfy conditions given by the user.
    chosen_words = []
    for ori in origins:
        for dif in difficulties:
            chosen_words += find_words(ori, dif, df)

    # Shuffling the chosen words (in place).
    random.shuffle(chosen_words)
    #print chosen_words

    # The quiz starts.
    # User input: n (default), u (difficulty level up), 
    #             d (difficulty level down), q (quit)
    if len(chosen_words) < num_words: # Find the number of words to quiz
        num_words = len(chosen_words)
    for i, word in enumerate(chosen_words):
        origin = origins_all[df.ix[word, 0] - 1]
        difficulty = df.ix[word, 1]
        # print word, origin, difficulty
        print "----------------------------------------------------------"
        print "word: " + word + " (Origin: " + origin + ", Difficulty: " \
            + str(difficulty) + ")" + "(" + str(i + 1) + " of " + \
            str(num_words) + ")"
        print "----------------------------------------------------------"
        user_input = "next" # default input
        if difficulty % 2:
            user_input = raw_input(
                    "Type u for difficulty level up, q for quit: ")
        else:
            user_input = raw_input(
                    "type d for difficulty level down, q for quit: ")
        user_input = user_input.strip()
        if difficulty % 2:
            if user_input == "u":
                df.ix[word, 1] = difficulty + 1
        else:
            if user_input == "d":
                df.ix[word, 1] = difficulty - 1
        if user_input == "q" or i == num_words - 1:
            break

    # Write the changes
    write_words(word_filename, df)

if __name__ == "__main__":
    main()
