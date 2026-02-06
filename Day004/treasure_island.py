# Project_004
print(r'''
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
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
while True:
  print("                   WELCOME TO TREASURE ISLAND                         \n")
  print("-> Your Mission is to find the Treasure <-\n")
  print("You're at a Cross road, where do you want to go?\n")
  user_choice = input("-> Type 'Left' or 'Right'\n")
  if user_choice == "Left":
    print("You've come to a lake. There is an island in the middle of the lake.\n")
  else:
    print("You've fallen in a pit. Game OVER!\n")
    break


  user_choice = input("-> Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")

  if user_choice == "wait":
    print("You arrived at the island unharmed. There is a house with 3 doors.\n")
  else:
    print("Shark has eaten you. Game OVER!\n")
    break

  user_choice = input("-> One red, one yellow and one blue. Which color do you choose?\n")

  if user_choice == "red":
    print("Treasure FOUND!\n")
    break
  elif user_choice == "yellow":
    print("The floor is LAVA!\n")
    break
  else:
    print("Fake Treasure\n")
    break
