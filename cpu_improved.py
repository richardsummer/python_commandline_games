import random

# name = input("Greetings human! What is your name: ")

print("Hello, " + "! \n Please enter a number between 1 and 100. \n I will guess it!")
number = int(input())

guess = 50

while guess != number:
    if guess < number:
        newGuess = guess
        print(newGuess)



# while guess != number:
#     if guess < number:
#         guess = random.randint(1, 100)
#         print(guess)
#     elif guess > number:
#         guess = random.randint(1, 100)
#         print(guess)
#     elif guess == number:
#         break

print("Ah ha! I knew the number was " + str(guess) + "!")
