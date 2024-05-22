'''
This Python program implements the Caesar Cipher encryption and decryption technique.
It allows users to encrypt or decrypt messages using a specified shift value.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = (position - shift_amount) % len(alphabet)
      end_text += alphabet[new_position]
    else: # if not a letter in alphabet, then don't change them!
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

# logo
from art import logo
print(logo)

# restart the cipher program?
# creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:
    # input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # call function
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # ask if they want to restart the cipher program?
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
