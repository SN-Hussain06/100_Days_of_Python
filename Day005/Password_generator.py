# Project_005
import random

print(r'''
                         .--------.
                        / .------. \
                       / /        \ \
                       | |        | |
                      _| |________| |_
                    .' |_|        |_| '.
                    '._____ ____ _____.'
                    |     .'____'.     |
                    '.__.'.'    '.'.__.'
                    '.__  |      |  __.'
                    |   '.'.____.'.'   |
                    '.____'.____.'____.'
                    '.________________.'
''')
print()
print("               * Python Password Generator *\n")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
nums = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']

user_letters = int(input("How many letters would you like in your password: "))
user_nums = int(input("Enter the number of digits: "))
user_symbols = int(input("Enter the number of symbols: "))

pass_word = []
for i in range(0,user_letters):
  pass_word.append(random.choice(letters))
for j in range(0,user_nums):
  pass_word.append(random.choice(nums))
for k in range(0,user_symbols):
  pass_word.append(random.choice(symbols))

size = user_letters + user_nums + user_symbols

print()
for val in range(0,size):
  print(" " + random.choice(pass_word), end="")


