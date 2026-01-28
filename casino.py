from numpy import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as rand
import csv


print(" █████╗ ██████╗ ██╗  ██╗     ██████╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗ ")
print("██╔══██╗██╔══██╗╚██╗██╔╝    ██╔════╝██╔══██╗██╔════╝██║████╗  ██║██╔═══██╗")
print("███████║██████╔╝ ╚███╔╝     ██║     ███████║███████╗██║██╔██╗ ██║██║   ██║")
print("██╔══██║██╔══██╗ ██╔██╗     ██║     ██╔══██║╚════██║██║██║╚██╗██║██║   ██║")
print("██║  ██║██║  ██║██╔╝ ██╗    ╚██████╗██║  ██║███████║██║██║ ╚████║╚██████╔╝")
print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ")


 ####################### login functions ####################### 


def login():
    username = input("Username: ")
    password = input("Password: ")

    with open("users.csv", mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["username"] == username and row["password"] == password:
                print("Login successful")
                return username

    print("Wrong username or password")
    return None

currect_user = None
while True:
    currect_user = login()
    if currect_user:
        break

 ####################### balance functions ####################### 

def get_balance(username):
    df = pd.read_csv("users.csv")
    user_row = df[df['username'] == username] 
    return int(user_row["moeny"].values[0])
     
def update_balance(username, new_balance):
    df = pd.read_csv("users.csv")
    df.loc[df['username'] == username, 'moeny'] = new_balance
    df.to_csv("users.csv", index=False)


 ####################### game functions ####################### 


def main():
    current_balance = get_balance(currect_user)
    history = [current_balance] 
    while True:
        print("current balance: ", current_balance)

        print("1.Random number game")
        print("2.slot machine")
        print("3.Roulette Simulator")
        print("4.exit")



        try:
            fav_Game = int(input("choose your favourite game (1 - 4):"))

            if fav_Game == 1:
                number = int(input("enter your lucky number! max is 50  : "))
                randomnumber = random.randint(50, size = (10))

                if number in randomnumber:
                    print("you won")
                    balance = get_balance(currect_user)
                    new_balance = balance + 2000
                    update_balance(currect_user, new_balance)

                else:
                    print("you lost ")
                    balance = get_balance(currect_user)
                    new_balance = balance - 500
                    update_balance(currect_user, new_balance)

                print("your lucky numbers was : ", randomnumber)

            elif fav_Game == 2:

                symbols = ["🍒", "🍋", "🔔",]
                input("Press Enter to spin...")
                slot1 = rand.choice(symbols)
                slot2 = rand.choice(symbols)
                slot3 = rand.choice(symbols)


                print(slot1, slot2, slot3)

                if slot1 == slot2 == slot3:
                    print("you won")
                    balance = get_balance(currect_user)
                    new_balance = balance + 5000
                    update_balance(currect_user, new_balance)

                elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
                    print("small win but win")
                    balance = get_balance(currect_user)
                    new_balance = balance + 2000
                    update_balance(currect_user, new_balance)
                else:
                    print("you lost")
                    balance = get_balance(currect_user)
                    new_balance = balance - 1000
                    update_balance(currect_user, new_balance)
        

            elif fav_Game == 3:

                # basic rules
                red_numbers = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,28,30,32,34,36]
                black_numbers = [2,4,6,8,10,11,13,15,17,20,22,24,26,29,31,33,35]

                bet = input("bet on red or black: ").lower()

                asshole = random.randint(36)

                # color
                if asshole == 0 :
                    color = "green"
                if asshole in red_numbers:
                    color = "red"
                if asshole in black_numbers:
                    color = "black"

                # win or not
                if bet == asshole:
                    print("you won")
                    balance = get_balance(currect_user)
                    new_balance = balance + 2000
                    update_balance(currect_user, new_balance)

                elif bet == "green":
                    print("you won")
                    balance = get_balance(currect_user)
                    new_balance = balance + 500
                    update_balance(currect_user, new_balance)
                else:
                    print("you lost")
                    balance = get_balance(currect_user)
                    new_balance = balance - 500
                    update_balance(currect_user, new_balance)

                # result 
                print("the number was : ", asshole)
                print("the color was : ", color)
        
                current_balance = new_balance 
                history.append(new_balance)
                
                if current_balance <= 0:
                    print("YOU ARE BROKE! GAME OVER!")
                    break

            elif fav_Game == 4:
                break

            else : 
                print("Please enter a number between 1 - 4")

        except Exception as e:  
            print("An unexpected error occurred: ", e)


      ################# GRAPH CODE #################
    print("\nGenerating your money graph...")
    try:
        theme = dict(color="r", marker='o', linestyle='-')
        plt.plot(history, **theme)
        plt.title(f"{currect_user}'Casino Session")

        plt.xlabel("Games Played")
        plt.ylabel("Money ($)")
        plt.grid(True)
        plt.show()

    except Exception as e:
        print("Could not show graph:", e)

main()


# HELP FROM AI WAS ABOUT THE MOENY SYSTEM 60
# HELP FROM AI WAS ABOUT THE GRAPH SYSTEM 10% (just asking what to print)
# HELP FROM AI WAS ABOUT THE LOGIN SYSTEM 70%

# HELP FROM AI WAS TOTAL : 30%