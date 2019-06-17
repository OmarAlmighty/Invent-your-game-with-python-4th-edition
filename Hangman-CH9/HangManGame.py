import random
# invent your game with python book
HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
O   |
    |
    |
   ===''', '''
+---+
O   |
|   |
    |
   ===''', '''
 +---+
 O   |
/|   |
     |
    ===''', '''
 +---+
  O  |
 /|\ |
     |
    ===''', '''
 +---+
 O   |
/|\  |
/    |
    ===''', '''
 +---+
 O   |
/|\  |
/ \  |
    ===''', '''          
  +---+
 [O   |
 /|\  |
 / \  |
     === ''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     === '''
                ]
words = {'Colors': 'red orange yellow green blue indigo violet white blackbrown'.split(),
         'Shapes': 'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits': 'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Animals': 'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}


def getRandomWord(wordDic):
    wordKey = random.choice(list(wordDic.keys()))
    wordInd = random.randint(0, len(wordDic[wordKey]) - 1)
    return [wordDic[wordKey][wordInd], wordKey]


def displayBoard(misedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(misedLetters)])
    print()
    print('Missed Letters:', end=' ')
    for l in misedLetters:
        print(l, end=' ')
    print()
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for l in blanks:
        print(l, end=' ')
    print()


def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgian():
    print('Do You want to play again(yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')
difficulty = ' '
while difficulty not in 'EMH':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')
    difficulty = input().upper()
    if difficulty == 'M':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
    if difficulty == 'H':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]
correctLettes = ''
missedLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set of ' + secretSet)
    displayBoard(missedLetters, correctLettes, secretWord)
    guess = getGuess(missedLetters + correctLettes)
    if guess in secretWord:
        correctLettes = correctLettes + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLettes:
                foundAllLetters = False
                break
        if foundAllLetters:
                print('Yes! The secret word is "' + secretWord +
                      '"! You have won!')
                gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLettes, secretWord)
            print('You have run out of guesses!\nAfter ' ,
                  str(len(missedLetters)) , ' missed guesses and ' ,
                  str(len(correctLettes)) , ' correct guesses, the word was "' , secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgian():
            missedLetters = ''
            correctLettes = ''
            gameIsDone = False
            secretWord = getRandomWord(words)

        else:
            break
