# Easy Python Game: Guess the Number

import random

secret_number = random.randint(1, 10)

print("Welcome to Guess the Number!")
print("I'm thinking of a number from 1 to 10.")

guess = int(input("Take a guess: "))

if guess == secret_number:
    print("🎉 You got it!")
else:
    print("❌ Nope!")
    print("The number was:", secret_number)
