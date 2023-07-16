import time

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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
direction = input('You arrive at the island, two roads to the east and west. Where do you turn? "east" or "west"? \n').lower()
if direction == "west":
  decision = input('You arrive at the foot of a mountain, you see an axe, and a shovel. You can only pick up one. "Shovel" or "Axe"? \n').lower()
  if decision == "shovel":
    sub_decision = input('There is a grave right beside the mountain entrance. What would you like to do? "dig"? or "ignore"? \n').lower()
    if sub_decision == "ignore":
      print("You proceed to enter the mountain \n")
      fight = input('''Five cannibals! Living inside the mountain!\n 
                 \\\\\//////
     .-""-.     \\\\\\//////
    / _  _ \   [[[[[[[]]]]]]]]
    |(_)(_)|   /////////\\\\\\
    (  /\  )  //// ~0 ( 0~ \\\\
     L====J   //(,  8-_\-8 ,)\\
     `-..-`    //|\ .===. /|\\
      \\//        \ '===' /*
       ||          \__.__/
    _.=||=._   .---'@   @'---.
    /| || |\  /     '@ @'     \
      _||_   /    .   Y   .  _/\
     /  _))-'  /|'---{@}---'|\_/\
     |  _)  _.' |   --:--   | \  \
     \___)-'    |   --:--   |  \  \
      \nThey just sighted you. What do you do? fight? run? \n''').lower()
      if fight == "fight":
        print("You manage to defeat 3...\n")
        for seconds in range(3,0,-1):
          print(".\n")
          time.sleep(1)
        print("You are defeated by the other 2\n")
        print("Game over.\n")
      elif fight == "run":
        print("They chase you down and defeat you..\n")
        for seconds in range(3,0,-1):
          print(".\n")
          time.sleep(1)
        print("Game over.")
      else:
        print("You did not make a valid decision. Game over.\n")
    elif sub_decision == "dig":
      print("You could not find the treasure. Game over.\n")
    else:
      print("You did not make a valid selection. Game over.\n")
  elif decision == "axe":
      print("You proceed to enter the mountain \n")
      fight = input('''Five cannibals! Living inside the mountain!\n 
                 \\\\\//////
     .-""-.     \\\\\\//////
    / _  _ \   [[[[[[[]]]]]]]]
    |(_)(_)|   /////////\\\\\\
    (  /\  )  //// ~0 ( 0~ \\\\
     L====J   //(,  8-_\-8 ,)\\
     `-..-`    //|\ .===. /|\\
      \\//        \ '===' /*
       ||          \__.__/
    _.=||=._   .---'@   @'---.
    /| || |\  /     '@ @'     \
      _||_   /    .   Y   .  _/\
     /  _))-'  /|'---{@}---'|\_/\
     |  _)  _.' |   --:--   | \  \
     \___)-'    |   --:--   |  \  \
      \nThey just sighted you. What do you do? fight? run? \n''').lower()
      if fight == "fight":
        print("You manage to defeat 3...")
        for seconds in range(3,0,-1):
          print(".\n")
          time.sleep(1)
        print("You just defeated by the other 2!")
        for seconds in range(3,0,-1):
          print(".\n")
          time.sleep(1)
        print("You proceed to their encampent..")
        final_decision = input("There is a green tent, what do you do? enter? leave? \n").lower()
        if final_decision == "enter":
          print("Treasure found! You win!")
        elif final_decision == "leave":
          print("You did not find the treasure. Game over.\n")
      elif fight == "run":
        print("They chase you down and defeat you..")
        for seconds in range(3,0,-1):
          print(".\n")
          time.sleep(1)
        print("Game over.")
      else:
        print("You did not make a valid selection. Game over.\n")
  else:
    print("You did not make a valid selection. Game over.\n")
elif direction == "east":
  print('''
                   _____
              .-" .-. "-.
            _/ '=(0.0)=' \_
          /`   .='|m|'=.   `\
          \________________ /
      .--.__///`'-,__~\\\\~`
     / /6|__\// a (__)-\\\\
     \ \/--`((   ._\   ,)))
     /  \\  ))\  -==-  (O)(
    /    )\((((\   .  /)))))
   /  _.' /  __(`~~~~`)__
  //"\\,-'-"`   `~~~~\\~~`"-.
 //  /`"              `      `\
//
  \nPirates attack and kill your character! Game over.\n''')  
else:
  print(f"There is no way {direction}. Game over.")
