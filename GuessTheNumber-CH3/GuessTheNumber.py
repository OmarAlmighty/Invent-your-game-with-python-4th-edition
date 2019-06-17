# this is guess the number name
import random

guesses = 0

print("Hello, What's your name")
name = input()

print("Choose your level:\n1:Easy\n2:Intermediate\n3:Hard\n4:Very hard")
lvl = input()

if lvl == '1':
    number = random.randint(1, 20)
    print("Well, " + name + " i am thinking of a number between 1 and 20")
if lvl == '2':
    number = random.randint(1, 100)
    print("Well, " + name + " i am thinking of a number between 1 and 100")
if lvl == '3':
    number = random.randint(1, 1000)
    print("Well, " + name + " i am thinking of a number between 1 and 1000")
if lvl == '4':
    number = random.randint(1, 5000)
    print("Well, " + name + " i am thinking of a number between 1 and 5000")

for guesses in range(10):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("guess is too low.")
    if guess > number:
        print("guess is too high")
    if guess == number:
        break

if guess == number:
    guesses = str(guesses + 1)
    print('Good job, ' + name + '! You guessed my number in ' +
          guesses + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
