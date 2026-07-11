import random

# This will be the classic game of hangman where the player has to guess a word letter by letter and they get 6 chances before the game is over
# HANGMAN_PICS is a list that contains multiple multi-line strings. This works because lists can contain several other values within said list
# Note that the variable is in all caps. This is a constant variable which means it is supposed to to stay the same throughout the code no matter what. The all caps is meant to remind me that this variable should be constant

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

# Next up I create the variable words which contains a multi line string of all the word options that will be selected from
# At the end of my string I use the .split method. This is a method that works for strings and serves to split each entry up into its own individual string
# This allows me to basically just create a long list of words to then choose from later without having to seperate them myself

words = 'ant baboon badger bar bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

# The function getRandomWord will decide a secret word from my words list created above
# Within the parenthesis we have wordList and this will be the parameter. A parameter is a placeholder variable that the function getRandomWord will now expect to be given so it may return a value
# Now in the future when I call to run the getRandomWord function I must also tell it what it will be using as its "wordList" think of this as an x or a y in a math equation 

def getRandomWord(wordList):
    # within this function we are going to take our wordlist and use randint again to select a random word from this list. Within this we use 2 arguments 0, and -1 index of the list. Indexes start from 0 then go up for each entry respectively, meaning that in a list of 3 items the indexes will be 0, 1, 2. This is the reason we use -1 as the second argument. -1 index simply means the last item in the list, we use this because the list should be as long or as short as we want. Using -1 means that no matter the length of the list we will always use the last item in that list as the cutoff. We are using this with the built in len() function.
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

# Next up I need a function to print the hangman board on the screen. Within this I want to print the stage the player is at in the game as well as the correct and incorrect guesses they have taken. I will achieve this with the parameters of missedLetters, correctLetters, and secretWord. These will all be strings that contain the missedLetters, and correctLetters for the player to see. 

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    # this for loop will iterate over all of the characters in the string missedLetters and print them onto the screen. Having end=' ' will put them with a space between each one instead of creating a new line for each entry. This should make it easier to read the output
    for letter in missedLetters:
        print(letter, end=' ')
    print()

# This line will print the progress the player has made on the word. This should simply show underscores for the letters that have not been guessed yet, then as the player correctly guesses a letter, the blanks should be filled in with the correct letters to allow the player to visually their progress and potentially be able to guess the word
    blanks = '_' * len(secretWord)

# This for loop achieves the functionality explained above. This loop will iterate over each letter in secretWord, and then check if that letter exists in correctLetters
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
# If that letter is a correctLetter, then it should print that letter out in its respective place on the secretWord and retain all the blank slots otherwise. In practice if the letter is apple and the player guess a then the print output should be a____ (a followed by 4 underscore 'blank' spaces)
    for letter in blanks:
        print(letter, end=' ')
    print()

# The next function that will be needed is a function getGuess. This will called so the player can enter a letter to guess. This will take that input and return it as a string. It additionally ensures that the player types a valid letter before it returns
def getGuess(alreadyGuessed):
    # I start off with a while loop to continue to prompt the player to enter a valid letter that has not already been guessed before proceeding with the function
    while True:
        print('Guess a letter.')
        # Here the player is prompted to guess a letter. After that the built in lower() function is used to convert the entry into a lowercase letter in order to check it against the secretWord as everything is in lowercase
        guess = input()
        guess = guess.lower()
        # finally I am using a series of elif statements to verify that the input is valid. This code will run through each check step by step and will not proceed until it meets all the steps to get to the final else statement
        # Only one block in an elif statement can be executed, this will only proceed once a valid input has been entered.
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER')
            # Once a valid input was given, we will return the guess the player made in order to check if it is correct or incorrect
        else:
            return guess

# Finally the playAgain function will simply ask the player if they would like to play again after the game has ended. IF they say yes then I want to reset the game state back to the beginning and select a new random word. 
def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            if foundAllLetters:
                print('Yes! The secret word is ' + secretWord + '! You win!!!!')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was ' + secretWord + '.')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
        else:
            break
     