from art import logo
from replit import clear

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        index = alphabet.index(char)
        shifted_index = (index + shift_amount) % len(alphabet)
        end_text += alphabet[shifted_index]
    else:
        end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}.\n")

decision = 'yes'

while decision == 'yes':
    print(logo)
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    decision = input("Type 'yes', if you want to go again. Otherwise type 'no'\n").lower()
    if decision == 'yes':
        clear()
    else:
        print("Goodbye")
