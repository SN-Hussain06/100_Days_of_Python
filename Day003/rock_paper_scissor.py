# Project_003
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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_count = 0
comp_count = 0

display_List = [rock,paper,scissor]

while True:
  print("  --- ROCK  PAPER  SCISSOR ---  ")
  print()
  user_choice = int(input("Choose ( rock:0, paper:1, scissor:2, exit:3 ) = "))

  if user_choice == 3:
    break
  print("\n You -> ",user_count)
  print(display_List[user_choice])

  computer_choice = random.choice(display_List)
  print("Computer -> ", comp_count)
  print(computer_choice)

  if user_choice == 0 and computer_choice == paper:
    print("Lose")
    comp_count += 1
  elif user_choice == 1 and computer_choice == scissor:
    print("Lose")
    comp_count += 1
  elif user_choice == 2 and computer_choice == rock:
    print("Lose")
    comp_count += 1
  elif ((user_choice == 0 and computer_choice == rock) or (user_choice == 1 and computer_choice == paper) or
    (user_choice == 2 and computer_choice == scissor)):
    print("Draw")
  else:
    print("Win!")
    user_count += 1


