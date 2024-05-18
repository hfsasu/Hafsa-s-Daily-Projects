print(r'''*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

firstChoice = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" ')

if firstChoice == "left":
    secondChoice = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a '
                         'boat. Type "swim" to swim across.')
    if secondChoice == "wait":
        thirdChoice = input('You\'ve arrived at the island unharmed. There is a house within 3 doors. One red, '
                            'one yellow, and one blue. Which color do you choose?')
        if thirdChoice == "red":
            print("You've entered a room of fire. Game over!")
        elif thirdChoice == "yellow":
            print("You found the treasure! You win!")
        elif thirdChoice == "blue":
            print("You've entered a room of beasts. Game over!")
        else:
            print("You chose a door that doesn't exist. Game over!")

    elif secondChoice == "swim":
        print("You were attacked by an angry trout. Game over!")

    else:
        print("You made an invalid choice. Game over!")

elif firstChoice == "right":
    print("You fell into a hole. Game over!")

else:
    print("You made an invalid choice. Game over!")