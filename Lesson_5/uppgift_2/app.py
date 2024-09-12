"""
Uppgift 2: Tupler – Koordinater för Städer
1. Skapa en tuple som innehåller tre element: namn på en stad, latitud, och longitud.
2. Skriv ut informationen om staden.
3. Be användaren skapa tre tupler för tre olika städer och skriv ut dem.
"""

def city_coordinates():
  city_stockholm_info = ("Stockholm", "59.3293° N", "18.0686° E")
  
  print("--------------")
  print(city_stockholm_info)
  print("--------------")
  
  loop_count = 0
  
  while loop_count < 3:
    city_name = input("Enter the name of a city: ").strip()
    city_lat = input("Enter the latitude: ")
    city_lat += "° N"
    city_long = input("Enter the longitude: ")
    city_long += " ° E"
    city_info = (city_name, city_lat, city_long)
    print("--------------")
    print(city_info)
    print("--------------")
    loop_count += 1

  return

city_coordinates()
