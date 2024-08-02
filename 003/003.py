# Day 003 - Treasure Hunt Game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_ 
*******************************************************************************
      ''')

print("Welcome to TREASURE ISLAND !!!")
print("Your mission is to find the old TREASURE, buried somewhere on this island...")
print("Good luck, my brother... good luck!\n")

# First step
print("You are standing on a crossroad. Where you want to go?")
answer = input("Left or right? \n").lower()

if answer == "right" or answer != "left":
    print("You fell into big, dark hole...")
    print(" G A M E  O V E R ")
    exit()


# Second step

print("You are standing in front of a nice lake? What do you want to do?")
answer = input("swim or wait? \n").lower()

if answer == "swim" or answer != "wait":
    print("You are atacked by trout. And he WINS...")
    print(" G A M E  O V E R ")
    exit()

# Third step
    
print("You are standing in front of three doors. Which one you want to open?")
answer = input("Red, yellow or blue? \n").lower()

if answer == "yellow":
    print("\nYOU FOUND THE TREASURE !!!")
    print("I hope you will spend it wise.\n GOOD LUCK, MY FRIEND !!!")
    exit()
elif answer == "red":
    print("\nYou are burned by the fire!")
    print(" G A M E  O V E R ")
    exit()
elif answer == "blue":
    print("\nYou are eaten by the beasts!!!")
    print(" G A M E  O V E R ")
    exit()
else:
    print("\nYou are going home empty-handed !!!")
    print(" G A M E  O V E R ")




