#!/usr/bin/python3
import random, time, math
print("""   Welcome to the Python Number Guessing Game!
            Made by YASSINE Hamza
Please enter the range of numbers to guess from: 

Instructions:
- You should enter the lower bound and upper bound of the range you wanted.
- You need to guess a number in that range.
- But it is not easy to win, you have to guess in the minimum number of attempts!
- The minimum number of attempts depends upon range, so the bigger the range the more attempts you get.

Have fun!
""")

lower, upper = 0, 0
while True:
    try:
        lower, upper = int(input("Lowerbound: ")), int(input("Upperbound: "))
        break
    except ValueError as ve:
        print(f"Please enter valid number(s) for the lowerbound/upperbound.")

num = random.randint(lower, upper)
guess = int
attempts = 0
requirement = math.log2(upper - lower + 1)

print("\n\nGet ready! 3...")
time.sleep(1)
print("2..")
time.sleep(1)
print("1.")
time.sleep(1)
print("Go, Start!", end = " ")

while guess != num:
    guess = int(input("Guess: "))
    if guess > num:
        print("Try Again! You guessed too high")
    elif guess < num:
        print("Try Again! You guessed too low")
    attempts += 1

if attempts > requirement:
    print("""You got it right, but unfortunately you passed the minimum attempts.
Better Luck Next Time!""")
else:
    print("Congratulations! You won!")