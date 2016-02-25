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
# Difficulty
#   0: all
#   1: easy
#   2: medium (default)
#   3: challenging (given)
#

import sys
import pandas as pd

# For exception (will be used only for raising exception).
class RangeError(Exception):
    """
    User-defined exception for range errors.
    """
    pass

# Numbers of origins & difficulties are given.
num_origins = 14
num_difficulties = 3

# Filename for words (in csv, format: word, origin, difficulty, with header)
word_filename = 'words.csv'

def get_input():
    """
    Obtain the user input
    """
    print "Origin of words."
    print "   0: all (default)"
    print "   1: Arabic"
    print "   2: Asian"
    print "   3: Dutch"
    print "   4: Eponyms"
    print "   5: French"
    print "   6: German"
    print "   7: Greek"
    print "   8: Italian"
    print "   9: Japanese"
    print "   10: Latin"
    print "   11: New World"
    print "   12: Old English"
    print "   13: Slavic"
    print "   14: Spanish"
    print
    print "Difficulty of words."
    print "   0: all (default)"
    print "   1: easy"
    print "   2: medium"
    print "   3: challenging"

    print "Type a number, or a series of numbers seperated by white spaces."

    origins_str = raw_input("Enter origins: ")
    difficulties_str = raw_input("Enter difficulties: ")
    origins = origins_str.split()
    if len(origins) == 0: # no input, then the default value is assigned
        origins = ['0']
    difficulties = difficulties_str.split()
    if len(difficulties) == 0: # no input, then the default value is assigned
        difficulties = ['0']

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
    except ValueError:
        print "# Bad input. Type integers seperated by white spaces only."
        sys.exit()
    except RangeError:
        print "# Bad input: integers should be in range."
        print "             For origins, between 0 and", num_origins
        print "             For difficulties, between 0 and", num_difficulties
        sys.exit()
    return origins2, difficulties2

# Read word file.
def read_words(word_filename):
    """
    Reads the word file in csv format, and returns the pandas data frame.
    """
    df = pd.read_csv(word_filename)
    return df

# Write word file.
def write_words(word_filename, df):
    """
    Writes the word file in csv format.
    """
    df.to_csv(word_filename)
    return

def main():
    """
    main fucntion
    """
    # Read word data.
    df = read_words(word_filename)

    # Get user inputs for origins and difficulties
    origins, difficulties = get_input()
    print origins, difficulties

if __name__ == "__main__":
    main()
