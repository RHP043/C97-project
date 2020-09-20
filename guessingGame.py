import random

print("Guessing Game")
number = random.randint(1,9)
chances = 5
print("Guess a number between 1 and 9")
while chances>0:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("You Win!!")
        break
    elif guess < number:
        print("Your guess is too low, guess higher")
    else:
        print("Your guess was too high, guess lower")
    chances-=1

if not chances>0:
    print("You lose. the number is : ",number)