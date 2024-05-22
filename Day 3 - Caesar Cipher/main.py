alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# 1. Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
def encrypt(plain_text, shift_amount):  # will send the text to plain_text..
    cipherText = ""
    for letter in plain_text:  # go thru each letter
        position = alphabet.index(letter)  # get the letter's position in the alphabet
        newPosition = (position + shift_amount) % len(alphabet)  # if we go out of index: ex (25+5)%26 = 4  which is e
        newLetter = alphabet[newPosition]
        cipherText += newLetter
    print(f"The encoded text is {cipherText}")


# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(cipher_text, shift_amount):
    plainText = ""
    for letter in cipher_text:  # go thru each letter
        position = alphabet.index(letter)  # get the letter's position in the alphabet
        newPosition = (position - shift_amount) % len(alphabet)  # if we go out of index: ex (25+5)%26 = 4  which is e
        newLetter = alphabet[newPosition]
        plainText += newLetter
    print(f"The decoded text is {plainText}")

# Call the functions and pass in the user inputs
if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
