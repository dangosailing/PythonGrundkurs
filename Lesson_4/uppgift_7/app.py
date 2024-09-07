import recepie_modules
"""
7. Receptbok med modulär programmering
Skapa en modul som hanterar att lägga till recept (titel, ingredienser,
instruktioner).
En modul som söker efter ett recept baserat på titel.
En modul som listar alla sparade recept.
Huvudprogrammet ska fråga användaren vilken operation de vill utföra (lägga
till, söka eller lista recept).
"""

def recepie_book():
    user_choice = int(input("1) Create new recepie\n2) Search recepie\n3) List recepies\n4) Quit program\n"))
    recepie_list =[]
    while user_choice != 4:
        if user_choice == 1:
            recepie_list = recepie_modules.add_recepie(recepie_list)
            print("Recepie added")
            user_choice = int(input("1) Create new recepie\n2) Search recepie\n3) List recepies\n4) Quit program\n"))
        elif user_choice == 2:
            recepie_modules.search_recepie(recepie_list)
            user_choice = int(input("1) Create new recepie\n2) Search recepie\n3) List recepies\n4) Quit program\n"))
        elif user_choice == 3:
            recepie_modules.list_recepies(recepie_list)
            user_choice = int(input("1) Create new recepie\n2) Search recepie\n3) List recepies\n4) Quit program\n"))
        elif user_choice == 4:
            print("Closing program")
            break

recepie_book()