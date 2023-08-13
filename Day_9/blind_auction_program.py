from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

data = []

def getdata(name, bid): 
    competitors = {}
    competitors["name"] = name
    competitors["bid"] = bid
    data.append(competitors)


print(logo)
print("Welcome to the secret auction program.")
control = "yes"
while control == "yes":
    name = input("What is your name? ")
    bid = int(input("what's your bid? $"))
    getdata(name, bid)
    print("\n")
    
    control = (input("Are there any other bidders? 'yes' or 'no': \n")).lower()
    print(" ")
    if control == "yes":
        clear()

highest = 0

for user in data: 
    score = user["bid"]
    if score > highest:
        highest = score
        winner = user["name"]
        
print(f"The winner {winner} is  with a bid of ${score}.")

