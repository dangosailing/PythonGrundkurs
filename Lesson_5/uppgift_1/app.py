"""
Uppgift 1: Grundläggande Dictionaries – Hantera Elevers
Information
1. Skapa en tom dictionary.
2. Låt användaren mata in namn och ålder för tre elever.
3. Lägg till varje elev och deras ålder i dictionaryn.
4. Skriv ut alla elever och deras åldrar
"""

def student_manager():
  students = {}
  count = 0
  while count < 3:
    name = input("Enter student name: ").strip()
    age = int(input("Enter student age: "))
    students[name] = age
    count += 1
  return

student_manager()