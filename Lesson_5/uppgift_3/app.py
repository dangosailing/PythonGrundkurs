"""
Uppgift 3: Grundläggande Sets – Unika Färger
1. Skapa två sets, ett med färger från användaren och ett med fördefinierade färger (t.ex.
{"röd", "grön", "blå"}).
2. Visa alla unika färger genom att kombinera båda setsen (använd union-metoden).
3. Visa de färger som finns i båda setsen (intersection).
"""

def unique_color_sets():
  user_colors = set()
  set_colors = {"violet", "green", "blue"}
  
  loop_count = 0

  while loop_count < 3:
    user_colors.add(input("Enter a color: ").strip())
    loop_count += 1

  all_colors = user_colors.union(set_colors)
  shared_colors = user_colors.intersection(set_colors)
  unique_colors_user = user_colors.difference(set_colors)
  unique_colors_set = set_colors.difference(user_colors)

  print("----All colors----")
  print(all_colors)
  print("----Shared colors----")
  print(shared_colors)
  print("----Unique colors from user set----")
  print(unique_colors_user)
  print("----Unique colors from predefined set----")
  print(unique_colors_set)
  print("----------------------------")


  return

unique_color_sets()