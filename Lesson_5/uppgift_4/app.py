"""
Uppgift 4: Dictionary med Kontrollstrukturer – Födelsedagsbok
1. Skapa en tom dictionary där nycklar är personnamn och värden är deras födelsedatum.
2. Låt användaren mata in namn och födelsedatum för tre personer.
3. Skriv ut alla personer och deras födelsedatum.
4. Låt användaren mata in ett namn och kontrollera om personen finns i dictionaryn. Om de
finns, skriv ut deras födelsedatum.
"""

def birthday_book():
  birthdays = dict()
  loop_counter = 0
  while loop_counter < 3:
    name = input("Enter a name: ")
    dob = input("Enter a date of birth (day/month/year): ")
    birthdays[name] = dob
    loop_counter += 1
  for name, dob in birthdays.items():
    print(f"{name} is born {dob}")

  query_name = input("Enter a name to searach the birthday book: ")
  if query_name in birthdays:
    print(f"{query_name} was found and is born on {birthdays[query_name]} ")
  else:
    print(f"{query_name} not found in birthday book")

birthday_book()

