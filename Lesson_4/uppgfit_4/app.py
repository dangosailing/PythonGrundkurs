import user_modules
"""Skapa ett program uppdelat i tre filer:"""

"""En modul för att lägga till användare (med namn
och ålder) till en lista."""

"""En modul för att söka efter användare i listan och
returnera deras information."""

"""En modul för att skriva ut alla användare."""

"""Huvudprogrammet ska låta användaren välja vilken operation de vill utföra
(lägga till, söka eller visa alla användare)."""

def user_management():
  user_list = []
  user_choice = int(input("1) Add new user\n2) Find user by name\n3) List all users\n4) Quit program\n"))
  while user_choice != 4:
    if user_choice == 1:
      user_modules.add_user(user_list)
      print("User addded")
      user_choice = int(input("1) Add new user\n2) Find user by name\n3) List all users\n4) Quit program\n"))
    elif user_choice == 2:
      user_name = input("Enter a name to query: ")
      user_modules.search_user(user_list, user_name)
      user_choice = int(input("1) Add new user\n2) Find user by name\n3) List all users\n4) Quit program\n"))
    elif user_choice == 3:
      user_modules.print_users(user_list)
      user_choice = int(input("1) Add new user\n2) Find user by name\n3) List all users\n4) Quit program\n"))
    elif user_choice == 4:
      print("Closing program")
      break
  return None

user_management()