import random

name = input("Greetings human! What is your name: ")

print("Hello, " + name + "! \n Please enter a number between 1 and 100. \n I will guess it!")
number = int(input())

guess = random.randint(1, 10)

while guess != number:
    if guess < number:
        guess = random.randint(1, 10)
        print(guess)
    elif guess > number:
        guess = random.randint(1, 10)
        print(guess)
    elif guess == number:
        break

print("Ah ha! I knew the number was " + str(guess) + "!")
