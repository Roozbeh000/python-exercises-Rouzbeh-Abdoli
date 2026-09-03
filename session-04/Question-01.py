# Question 1
import random

number= random.randint(1, 100)
while True:
    guess = int(input("Guess the number:"))
    if guess > number:
        print("The number is smaller.")
    elif guess < number:
        print("The number is bigger.")
    else:
        print("Congrats, You guess the right number.")
        break