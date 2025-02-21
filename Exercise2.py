import random

#program that has user guess a random number
random_num = random.randint(0,100)
count = 0

while True:
    guess = int(input("Guess a number: \n"))
    if guess > random_num:
        print("guess lower")
        count = count + 1 
    elif guess < random_num:
        print("guess higher")
        count = count + 1
    else:
        print("Correct! Congrats :)")
        print("You have guessed " + str(count) + " times.")
        break
