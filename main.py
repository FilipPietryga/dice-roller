import random

n = random.randint(1,99)

while True:
    g = int(input("Guess a number: "))
    if g < n:
        print("the number is too small")
    elif g > n:
        print("the number is too big")
    if g == n:
        print("the number is ok :D - you have won!")
        break