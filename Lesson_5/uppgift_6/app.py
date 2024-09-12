"""
Uppgift 6: Sets – Fritidsintressen
1. Skapa två sets, ett med fritidsintressen för två personer.
2. Använd en for-loop för att skriva ut alla intressen för varje person.
3. Använd union och intersection för att visa unika och gemensamma intressen.
"""

def interests():
  interests_1 = {"python", "javascript", "running", "watching TV"}
  interests_2 = {"python", "javascript", "bouldering", "cooking food"}

  print("\n---------------- Person A ----------------")
  for interest in interests_1:
    print(interest, end=" | ")
  print("\n")
  print("\n---------------- Person B ----------------")
  for interest in interests_2:
    print(interest, end=" | ")
  print("\n")

  print("\n------------------------------- Interests -------------------------------")
  unique_interests = interests_1.union(interests_2)
  for interest in unique_interests:
    print(interest, end=" | ")
  print("\n")
  print("\n---------------- Common interests ----------------")
  shared_interests = interests_1.intersection(interests_2)
  for interest in shared_interests:
    print(interest, end=" | ")
  print("\n")

interests()