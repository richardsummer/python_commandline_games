import random

number = random.randint(1, 100)
number_of_guesses = 0

name = input("Hello! What is your name: ")

print(name + ", I am thinking of a number between 1 and 100. You have 5 guesses.\n What is your first guess?" )

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print("Nope, too low. \n Guess again!")
    if guess > number:
        print("Nope, too high. \n Guess again!")
    if guess == number:
        break

if guess == number: print("You guessed the correct number in " + str(number_of_guesses) + " guesses!")
else: print("Haha! You did not guess the correct number! It was " + str(number) + "! \n Try again next time!")
