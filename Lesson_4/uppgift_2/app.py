import filter_modules

def filter_list():
  user_text = input("Enter a number of comma-separated strings: \n")
  user_option = int(input("Select how you wish to modify the text\n1) Filter text for words containing a specific character\n2) Set max string length\n3) View list\n4) Quit program\n"))
  
  list_str = user_text.split(",")

  while user_option != 3:
    if user_option == 1:
      user_target_char = input("Enter a character to filter the strings by: \n")
      user_text = filter_modules.filter_str_char(list_str, user_target_char)
      print(user_text)      

    elif user_option == 2:
      user_str_max_len = int(input("What´s the limit of characters for the strgins: \n"))
      user_text = filter_modules.filter_str_len(list_str, user_str_max_len)
      print(user_text)      
      
    elif user_option == 3:
      print(user_text)
      break

    elif user_option == 4:
      print("Closing program")
      break

    user_option = int(input("Select how you wish to modify the text\n1) Filter text for words containing a specific character\n2) Set max string length\n3) View list\n4) Quit program\n"))

filter_list()