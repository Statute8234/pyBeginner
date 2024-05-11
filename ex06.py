# Exercise 6
## Objective: using the function combine(word1, word2) from ex5.py, create a function counter(word) that will return the number of characters in the portmanteau

import ex05

def counter(word1,word2):
    string = ex05.combine(word1,word2)
    return len(string)