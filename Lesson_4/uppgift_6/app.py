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
    filename = text_editor_modules.write_note()
    text_editor_modules.read_note(filename)
    text_editor_modules.clear_note(filename)
    return

text_editor()