import todo_modules
"""Dela upp programmet i moduler:
En modul för att lägga till nya uppgifter.
En modul för att markera uppgifter som klara.
En modul för att ta bort uppgifter.
En modul för att visa uppgifter
Använd en lista för att lagra uppgifterna och en while-loop för att hålla
programmet interaktivt tills användaren väljer att avsluta."""

def todo_list():
  new_list = []
  user_choice = int(input("1) Add new task\n2) Mark task as done\n3) Remove task\n4) List tasks\n5) Clear done tasks from list\n6) Quit program\n"))
  while user_choice != 6:
    if user_choice == 1:
      new_list = todo_modules.enumerate_tasks(todo_modules.add_task(new_list))
      print(new_list)
      user_choice = int(input("1) Add new task\n2) Mark task as done\n3) Remove task\n4) List tasks\n5) Clear done tasks from list\n6) Quit program\n"))
    elif user_choice == 2:
      new_list = todo_modules.toggle_done(new_list)
      print(new_list)
      user_choice = int(input("1) Add new task\n2) Mark task as done\n3) Remove task\n4) List tasks\n5) Clear done tasks from list\n6) Quit program\n"))
    elif user_choice == 3:
      new_list = todo_modules.enumerate_tasks(todo_modules.remove_task(new_list))
      print(new_list)
      user_choice = int(input("1) Add new task\n2) Mark task as done\n3) Remove task\n4) List tasks\n5) Clear done tasks from list\n6) Quit program\n"))
    elif user_choice == 4:
      todo_modules.list_tasks(new_list)
      user_choice = int(input("1) Add new task\n2) Mark task as done\n3) Remove task\n4) List tasks\n5) Clear done tasks from list\n6) Quit program\n"))
    elif user_choice == 5:
      new_list = todo_modules.enumerate_tasks(todo_modules.clear_done_tasks(new_list))
      print(new_list)
      user_choice = int(input("1) Add new task\n2) Mark task as done\n3) Remove task\n4) List tasks\n5) Clear done tasks from list\n6) Quit program\n"))
    elif user_choice == 6:
      print("Closing program")
      break

todo_list()