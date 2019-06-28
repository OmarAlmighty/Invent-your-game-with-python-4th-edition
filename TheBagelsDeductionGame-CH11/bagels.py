import random

NUM_DIGIT = 3
MAX_GUESS = 10


# Returns a string of unique random digits that is NUM_DIGITS long.
def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGIT):
        secretNum += str(numbers[i])
    return secretNum


# Returns a string with the Pico, Fermi, & Bagels clues to the user.
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'

    clues.sort()
    return ' '.join(clues)


# Returns True if num is a string of only digits. Otherwise, returns False.
def isOnlyDigits(num):
    if num == '':
        return False
    for i in num:
        if i not in '1 2 3 4 5 6 7 8 9 0'.split():
            return False

    return True


print('I am thinking of a %s-digit number. Try to guess what it is.' % (NUM_DIGIT))
print('The clues I give are...')
print('When I say: That means:')
print(' Bagels None of the digits is correct.')
print(' Pico One digit is correct but in the wrong position.')
print(' Fermi One digit is correct and in the right position.')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' %(MAX_GUESS))
    gussesTaken = 1
    while gussesTaken <= MAX_GUESS:
        guess = ''
        while len(guess)!= NUM_DIGIT or not isOnlyDigits(guess):
            print('Guess #%s' %(gussesTaken))
            guess = input()
        print(getClues(guess,secretNum))
        gussesTaken += 1
        if guess == secretNum:
            break
        if gussesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.'% (secretNum))


    print('Do you want to play again(yes or no)')
    if not input().lower().startswith('y'):
        break