import random
import time

def generate_wheel():
    spaces = []
    for i in range(18):
        spaces.append("red")
        spaces.append("black")
    for i in range(2):
        spaces.append("green")
    return spaces

def spint_wheel(spaces):
    return random.choice(spaces)

def play_game():
    spaces = generate_wheel()
    
    money = 1000

    while True:
        print("You have $" + str(money) + ". Be careful ;)")

        bet = input("How much do you want to bet? ")
        bet = int(bet)
        color = input("What color will you bet on? ")

        print("The wheel is spinning...")
        time.sleep(2)

        landed = spint_wheel(spaces)
        print("it landed on " + landed)
        if color == landed:
            money = money + bet
            print("Congrats! You now have $" + str(money))
        elif color != landed:
            money = money - bet
            print("Whomp whomp, you now has $" + str(money))
    
        play_game = input("Do you want to play again?")
        if play_game == "no":
            break


play_game()