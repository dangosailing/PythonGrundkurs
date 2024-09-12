"""
Uppgift 7: Dictionary med Flera Nyckel-Värde-Par – Bokhylla
1. Skapa en dictionary där nycklar är bokkategorier och värden är listor av böcker.
2. Låt användaren mata in böcker i olika kategorier.
3. Skriv ut alla böcker i en specifik kategori baserat på användarens val.
"""

def book_shelf():
  shelf = dict()
  user_choice = int(input("1) Add new category\n2) Add books to category\n3) List books in cateogry\n4) Quit program\n>>> "))
  while True:
    if user_choice == 1:
      category = input("Enter a category to add:\n >>> ")
      shelf[category] = []
      print("------------------")
      user_choice = int(input("1) Add new category\n2) Add books to category\n3) List books in cateogry\n4) Quit program\n>>> "))
    elif user_choice == 2:
      category = input("Enter a category to add books to:\n >>> ")
      books = input("Enter a comma separated list of books:\n >>> ").split(",")
      shelf[category] = books
      print("------------------")
      user_choice = int(input("1) Add new category\n2) Add books to existing category\n3) List books in cateogry\n4) Quit program\n>>>"))
    elif user_choice == 3:
      category = input("Enter a category to list all available books:\n >>> ")
      if category in shelf and len(shelf[category]) > 0:
        for books in shelf[category]:
          print(books, end=" | ")
      else: 
          print("Category not found or empty")
      print("\n------------------")
      user_choice = int(input("1) Add new category\n2) Add books to existing category\n3) List books in cateogry\n4) Quit program\n>>>"))
    elif user_choice == 4:
      break

book_shelf()
    


