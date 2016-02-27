# Spelling Tester
This small program is created to help my daughter to practice for her spelling
bee competition.

We were given a list of words with origins:

1. Arabic (52+31)
2. Asian (34+20)
3. Dutch (80+19)
4. Eponyms (37+16)
5. French (68+24)
6. German (60+19)
7. Greek (118+23)
8. Italian (69+19)
9. Japanese (35+5)
10. Latin (121+23)
11. New World (47+9)
12. Old English (89+7)
13. Slavic (41+11)
14. Spanish (60+12)

In the given list, words are divided into two groups: normal words and
challenge words (sizes are represented by two numbers in parentheses).
An origin is an attribute of a given word, and here I added another attribute
called *difficulty*, which a user can set. Initially normal words are set as
2, and challenge words as 4. Difficulty is the way for users to set aside
easy words, so normal words can be downgraded to 1, and challenge words to 3,
if a user feels those words are easy. For simpliciy, we assume normal words can
only have 1 or 2, and chanllenge words 3 or 4.

Now a helper can generate shuffled words using the origin and the difficulty level. 
Then a helper can read the word one by one.
While running the program, a user can change the difficulty level, or quit at any word.
If 'quit' is chosen, or all the chosen words are used, changed difficulty
levels will be saved to a file.

I used python with pandas.
