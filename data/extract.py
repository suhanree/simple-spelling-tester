# This program extracts words from given data files, and store them in a csv
# file.

def main():
    """
    Main function
    """

    # Filenames
    input_filenames = ['words_arabic', 'words_dutch', 'words_french',
        'words_greek', 'words_japanese', 'words_new_world', 'words_slavic',
        'words_asian', 'words_eponyms', 'words_german', 'words_italian',
        'words_latin', 'words_old_english', 'words_spanish']

    output_filename = 'words.csv'
    
    # opening csv file.
    f_csv = open(output_filename, 'wb')
    f_csv.write('word,origin,difficulty\n')   # header

    # Reading all input files and extracting words.
    for i, filename in enumerate(input_filenames):
        print i+1, filename
        filename = input_filenames[i]
        with open(filename) as f:
            difficulty = 2  # initial difficulty level
            for line in f:
                words = line.strip().split()
                if 'Challenge' in words: # From here on, challenge words (level: 3)
                    difficulty = 3  
                else:
                    print words[0]+','+ str(i+1) + ',' + str(difficulty)
                    f_csv.write(words[0]+','+ str(i+1) + ',' + str(difficulty)
                            + '\n')

if __name__ == "__main__":
    main()
