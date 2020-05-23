import pandas as pd
import csv
import os

file = open(os.path.join("C:/Users/exzac/Desktop", "XwiWordList.csv"))
reader = csv.reader(file, delimiter='\n')



# Moves all elements from the CSV file into a single list (as opposed to a list of lists)
uncutList = []
for word in reader:
    uncutList.append(word[0])

# Removes the word's score (example line in CSV file: lampshade;60) from the word and recreates a list
cutList = []
for word in uncutList:
    splitGroups = str(word).split(';')
    cutList.append(splitGroups[0])
 
# Updates the reader list to the newly cut list
reader = cutList

#Makes it easier to use a specific function
funcs = [(0, 'Find letters at specific positions'), (1, 'Find words with letters in specific sequences')]

# chooseFunc algorithm - the "home page", allows the user to select which program function they want
def chooseFunc():
    print('!===START FUNCTIONS===!\n')
    for func in funcs:
        print(str(func[0]) + ' | ' + func[1])
    print('\n!===END FUNCTIONS===!\n')
    selectedFunc = int(input('Choose: '))
    useFunc(selectedFunc)

# printWords algorithm - to print the resulting words to the screen
def printWords(printed, col, multiplier=1):
    count = 0
    for word in printed:
        if (count % int(col) == 0):
            print('\n')
        ending = '\t'*multiplier
        print(word, end=ending)
        count += 1
    print('\n\n')

def useFunc(funcNum):
    if (funcNum == 0):
        def letterAt(wordlist):

            letter = input('What letter? ').lower()
            loc = int(input('Where is its location in the word? '))

            words = []

            for word in wordlist:
                if(len(word) >= loc):
                    if(letter == word[loc-1]):
                        words.append(word)
    
            col = input('How many columns would you like to print with? ')
            print('\n\n')
            if(len(words) != 0):
                print('!===START LIST===!\n')
                printWords(words, col)
                print("\n!===END LIST===! \n\n")
    
            if(len(words) > 2):
                narrow = input('Narrow down responses? y/n: ')
                if (narrow == 'y'):
                    letterAt(words)

    
            tryAgain = input('Go again? y/n: ')
            if (tryAgain == 'y'):
                letterAt(reader)
            else:
                chooseFunc()

        letterAt(reader)

    # If the user chooses to find letters in specific sequences:
    elif (funcNum == 1):
        # letterSequence algorithm - finds words with letters in specific sequences
        def letterSequence(wordlist):

            query = input('Write a sequence of letters using \'?\' for single unknown letters: ').lower()
            queryLen = len(query)
            words = []

            for word in wordlist:
                if(len(word) == queryLen):
                    print(word + ' added: length')
                    words.append(word)
            print(words)

            # Sub-algorithm that searches through the wordlist and removes words that don't fit the criteria
            deselectedWords = []
            for i, letter in enumerate(query):
                if(letter != '?'):
                    for j, word in enumerate(words):
                        print('checking ' + word + ' for inequality')
                        if (word[i] != letter):
                            print(word + ' popped: inequality')
                            deselectedWords.append(word)
                    words = list(set(words) - set(deselectedWords))
            
            col = input('How many columns would you like to print? ')
            if(queryLen > 6):
                multiplier = 2
            else:
                multiplier = 1

            # Sub-algorithm that prints words to the screen
            printWords(words, col, multiplier)

            tryAgain = input('Go again? y/n: ')
            if (tryAgain == 'y'):
                letterSequence(reader)
            else:
                chooseFunc()
    
        letterSequence(reader)

chooseFunc()