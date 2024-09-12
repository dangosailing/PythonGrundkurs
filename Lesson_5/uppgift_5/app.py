"""
Uppgift 5: Tupler – Koordinater för Platser
1. Skapa en tuple som representerar latitud och longitud för en plats.
2. Skriv ut informationen om platsen.
3. Skapa en lista med tre tupler som representerar koordinaterna för tre olika platser (t.ex.,
städer eller intressanta platser).
4. Iterera över listan och skriv ut informationen om varje plats.
"""

place_1 = ("Harajuku", "35.6700° N", "139.7090° E")
place_2 = ("London Bridge", "51.5079°", "N, 0.0877° W")
place_3 = ("Empire State Building", "40.7484° N", "73.9857° W")
place_4 = ("Statue of Liberty", "40.6892° N", "74.0445° W")

places = [place_1,place_2,place_3,place_4]

for place in places:
  print(place)
