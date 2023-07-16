#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#generate random letters based on the number of letters requested by the user
gen_letters = ""
for i in range(0, nr_letters):
  gen_letters += random.choice(letters)
# print(gen_letters)

#generate random symbols based on the number of symbols requeted by the user
gen_symbols = ""
for j in range(0, nr_symbols):
  gen_symbols += random.choice(symbols)
# print(gen_symbols)

#generate random symbols based on the number of numbers requested by the user
gen_numbers = ""
for k in range(0, nr_numbers):
  gen_numbers += random.choice(numbers)
# print(gen_numbers)

#concatenant the letters, symbols and number generated
result = gen_letters + gen_symbols + gen_numbers

#randomly switch the characters to produce a password
password = ''.join(random.sample(result, len(result)))

# print(result)
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
