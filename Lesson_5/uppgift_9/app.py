"""
Uppgift 9: Kombinera Tupler och Dictionaries – Personregister
1. Skapa en dictionary där varje nyckel är en persons namn och värdet är en tuple med ålder
och stad.
2. Låt användaren mata in information om tre personer.
3. Skriv ut alla personer och deras information.
4. Använd en for-loop för att skriva ut namnen på personer som är äldre än 30 år.
"""

def person_register():
  persons = dict()

  loop_counter = 0

  while loop_counter < 3:
    person_name = input("Enter a user name: ")
    person_age = int(input("Enter age: "))
    person_city = input("Enter location: ")
    persons[person_name] = (person_age, person_city)
    loop_counter += 1

  for person in persons:
    print(f"{person} | age:{person[0]} | location: {person[1]}")
  
  control_age = 30

  for person in persons:
    if persons[person][0] > control_age:
      print(f"{person} is older than {control_age}")

  

person_register()


