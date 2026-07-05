import random
HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
o   |
    |
    |
   ===''', '''
+---+
o   |
|   |
    |
   ===''','''
+---+
 o  |
/|  |
    |
   ===''','''
+---+
 o  |
/|\ |
    |
   ===''','''
+---+
 o  |
/|\ |
/   |
   ===''','''
+---+
 o  |
/|\ |
/ \ |
   ==='''  ]

words = 'ant baboon badger bar bear beaver camel cat clam cobra cougar coyote crow deer fog donker duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

def getRandomWords(wordList):
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()