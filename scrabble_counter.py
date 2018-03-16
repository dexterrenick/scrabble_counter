#!/usr/bin/env python3

__author__ = "Dexter Renick"
__version__ = "2018-02-2"

import time

def main():
    time_initial = time.time()
    filename = "aliceinwonderland.txt"
    infile = open(filename,"r")
    wordlist = infile.readlines() #seperates each word by line
    infile.close()
    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i].lower().rstrip() #removes extra text string at the end
    letters = []
    for word in wordlist:
        for letter in word:
            letters.append(letter.lower())
    # Put the letters into a dictonary by frequency count
    letter_counts = {}
    for letter in letters:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    time_final = time.time()
    print("Time elapsed:",time_final-time_initial)
    # Print out the results
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for alphabetletter in alphabet:
        print(alphabetletter,":", letter_counts[alphabetletter])




if __name__ == "__main__":
    main()
