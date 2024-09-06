import text_modules

def text_converter():
  user_text = input("Please enter a text string:\n")
  user_option = 0
  while user_option != 3:
    if user_option == 1:
      user_text = text_modules.text_to_upper(user_text)
      print(user_text)
    elif user_option == 2:
      user_text = text_modules.strip_spaces(user_text)
      print(user_text)
    elif user_option == 3:
      print("Closing program")
      break

    user_option = int(input("Select how you wish to modify the text\n1)Convert to upper case\n2)Remove all spaces\n3)Quit program\n"))

text_converter()