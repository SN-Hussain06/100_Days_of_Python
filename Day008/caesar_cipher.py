#Project 008
def caesar():

  def encrypt(original_text):
    shift = int(input("Enter the number of shift: "))
    encrypted_text = ""

    for i in range(0,len(original_text)):

      if original_text[i] == " ":
        encrypted_text += " "
      # ord("character") converts letter to ascii(no.) , chr(no.) converts ascii to letter
      else:
          num = ord(original_text[i])
          encrypted_text += chr(num + shift)
    return encrypted_text

  def decrypt(original_text):
    shift = int(input("Enter the number of shift: "))
    decrypted_text = ""

    for i in range(0,len(original_text)):
      if original_text[i] == " ":
        decrypted_text += " "
      else:
        decrypted_text += chr(ord(original_text[i]) - shift)
    return decrypted_text

  user_choice = input("Type 'encode' to encrypt the message or 'decode' to decrypt the message: ")
  user_message = input("Message -> ")
  if user_choice == "encode":
      print("encoded message -> " + encrypt(user_message))
  elif user_choice == "decode":
      print("decoded message -> " + decrypt(user_message))
  else:
    print("Invalid choice!")
  user_choice = input("Type 'yes' to run again or 'no' to exit: ")
  if user_choice == "yes":
    caesar()
  else:
    print("Ended")

print(
    r'''
,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
 '''
)
print(
    r'''
   _____ _       _
  / ____(_)     | |
 | |     _ _ __ | |__   ___ _ __
 | |    | | '_ \| '_ \ / _ \ '__|
 | |____| | |_) | | | |  __/ |
  \_____|_| .__/|_| |_|\___|_|
          | |
          |_|
''')
caesar()