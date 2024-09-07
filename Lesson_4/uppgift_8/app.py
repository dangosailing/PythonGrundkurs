import contact_modules

"""
8. Kontaktbok med filhantering
Dela upp i moduler:
En modul för att lägga till nya kontakter (namn
och telefonnummer) och spara dem i en fil.
En modul för att läsa och visa alla kontakter från
filen.
En modul för att söka efter en specifik kontakt i
filen.
Huvudprogrammet ska låta användaren välja vilken operation de vill utföra
"""

def contact_book():
    contact_list = []
    user_choice = int(input("1) Create new contact\n2) Search contacts by name\n3) List all contacts\n4) Quit program\n"))
    while user_choice != 4:
        if user_choice == 1:
            contact_modules.add_contact(contact_list)
            print("Contact added")
            user_choice = int(input("1) Create new contact\n2) Search contacts by name\n3) List all contacts\n4) Quit program\n"))
            
        elif user_choice == 2:
            contact_modules.search_contacts(contact_list)
            user_choice = int(input("1) Create new contact\n2) Search contacts by name\n3) List all contacts\n4) Quit program\n"))
            
        elif user_choice == 3:
            contact_modules.list_contacts(contact_list)
            user_choice = int(input("1) Create new contact\n2) Search contacts by name\n3) List all contacts\n4) Quit program\n"))
            
        elif user_choice == 4:
            print("Closing program")
            break

contact_book()
