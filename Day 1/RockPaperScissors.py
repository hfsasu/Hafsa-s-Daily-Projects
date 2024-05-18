# In this program you play rock-paper-scissors with the computer
# You vs the computer
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

print("Welcome to the game")
human = int(input("Please type 0 for rock, 1 for paper, or 2 for scissors"))
computer = random.randint(0, 2)

print(f"Computer choose: {game_images[computer]}")
print(f"You choose: {game_images[human]}")

# Just printing the values - no images
# print(f"Computer choose: {computer}")
# print(f"You choose: {human}")

# Choosing Winners
if human not in [0, 1, 2]:
    print("You typed a wrong number. Please enter a number in the range of 0-2.")
else:
    if computer == human:
        print("It's a tie!")
    elif (human == 0 and computer == 2) or (human == 1 and computer == 0) or (human == 2 and computer == 1):
        print("You win!")
    else:
        print("Computer wins!")