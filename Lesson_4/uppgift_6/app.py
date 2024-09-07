import text_editor_modules

"""
Filbaserad textredigerare
Skapa ett program som låter användaren skriva anteckningar och spara dem i
en textfil. Använd tre moduler:
En för att skapa och skriva till filen.
En för att läsa från filen och visa innehållet.
En för att radera hela innehållet i filen.
Använd with open() för filhanteringen och låt användaren interagera med
programmet via ett huvudprogram
"""

def text_editor():
    user_choice = int(input("1) Create and/or write to file\n2) Read file contents\n3) Clear file contents\n4) Quit program\n"))
    filename = ""
    while user_choice != 4:
        if user_choice == 1:
            filename = text_editor_modules.write_note()
            user_choice = int(input("1) Create and/or write to file\n2) Read file contents\n3) Clear file contents\n4) Quit program\n"))
        elif user_choice == 2:
            if filename == "":
                filename = input("Enter the file to open: ")
            else:
                text_editor_modules.read_note(filename)
            user_choice = int(input("1) Create and/or write to file\n2) Read file contents\n3) Clear file contents\n4) Quit program\n"))
        elif user_choice == 3:
            if filename == "":
                filename = input("Enter the file to clear: ")
            else:
                text_editor_modules.clear_note(filename)
            user_choice = int(input("1) Create and/or write to file\n2) Read file contents\n3) Clear file contents\n4) Quit program\n"))
        elif user_choice == 4:
            print("Closing program")
            break

    return

text_editor()