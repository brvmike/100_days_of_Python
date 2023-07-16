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

#Write your code below this line 👇
import random
import time

choice = float(input("What do you choose? Type '0' for Rock, '1' for Paper, '2' for Scissors: \n"))

choice = round(choice)
choice = int(choice)

print(f"You chose '{choice}' \n")

while choice >= 3:
    choice = int(input("Wrong input, please type 0 for Rock, 1 for Paper, 2 for Scissors: \n"))

options = [rock, paper, scissors]

user_choice = options[choice]
print(user_choice)

length = len(options) - 1

computer_choice = random.randint(0, length)
shuffle = options[computer_choice]

for seconds in range(2,0,-1):
  print(".\n")
  time.sleep(1)
print(f"\ncomputer chose{shuffle}")

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

if shuffle == options[0] and user_choice == options[2]:
  print("You lose")
elif user_choice == options[0] and shuffle == options[2]:
  print("You win!")
elif shuffle == options[2] and user_choice == options[1]:
  print("You lose")
elif user_choice == options[2] and shuffle == options[1]:
  print("You win!")
elif shuffle == options[1] and user_choice == options[0]:
  print("You lose")
elif user_choice == options[1] and shuffle == options[0]:
  print("You win!")
else:
  print("It's a draw. let's try again..")

