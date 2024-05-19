import random
import hagman_art
import hangman_words

# word_list = ["zebra", "baboon", "camel"] # this line is when building the program for testing purposes
# print(f'The solution is {chosen_word}.') # Testing code
chosen_word = random.choice(hangman_words.word_list)
length = len(chosen_word)
lives = 6

print(hagman_art.logo)

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for x in range(length):
    display += "_"
print(display)

endOfGame = False
while not endOfGame:
    guess = input("Guess a letter: ").lower()
    if guess not in chosen_word:  #don't remove lives if the chosen letter is correct
        lives -= 1
        print("Your guess '" + guess + "' is not in the word.")
    elif guess in display:
        print("You've already guessed this letter correctly, guess again")
    print(hagman_art.stages[
              lives])  # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")
    print(display)

    if "_" not in display:  # if _ is not in the list
        endOfGame = True
        print("You win!!")
    elif lives == 0:
        endOfGame = True
        print("You lost :( The correct word was:", chosen_word)
