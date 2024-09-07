import library_modules
"""
9. Bibliotekssystem med flera filer
Skapa ett enkelt bibliotekssystem som är uppdelat i flera moduler:
En modul för att lägga till böcker (titel och
författare) i en lista.
En modul för att låna ut böcker och uppdatera
listan över tillgängliga böcker.
En modul för att returnera böcker och uppdatera
statusen för dessa.
Använd en huvudmodul som låter användaren hantera biblioteket.
"""

def library_manager():
    book_list = []
    user_choice = int(input("1) Add new book\n2) Lend book\n3) Return book\n4) Quit program\n"))
    while user_choice != 4:
        print("List out books in system")
        print(book_list)
        if user_choice == 1:
            library_modules.add_book(book_list)
            print("Book added")
            user_choice = int(input("1) Add new book\n2) Lend book\n3) Return book\n4) Quit program\n"))
        elif user_choice == 2:
            library_modules.lend_book(book_list)
            print("Book lended")
            user_choice = int(input("1) Add new book\n2) Lend book\n3) Return book\n4) Quit program\n"))
        elif user_choice == 3:
            library_modules.return_book(book_list)
            print("Book lended")
            user_choice = int(input("1) Add new book\n2) Lend book\n3) Return book\n4) Quit program\n"))
        elif user_choice == 4:
            print("Closing program")
            break

library_manager()