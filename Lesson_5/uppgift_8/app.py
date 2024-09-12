"""
Uppgift 8: Kontrollstrukturer och Dictionaries – Produktfiltrering
1. Skapa en dictionary där nycklar är produktnamn och värden är priser.
2. Låt användaren mata in produkter och deras priser.
3. Be användaren mata in ett maxpris och använd en for-loop och if-sats för att visa alla
produkter som kostar mindre än maxpriset.
"""

def product_filtering():
  products = dict()
  loop_counter = 0

  while loop_counter < 3:
    product_name = input("Enter the name of a product: ")
    product_price = float(input("Enter the price of the product: "))
    products[product_name] = product_price
    loop_counter += 1
  
  max_price = float(input("Enter a max price: "))

  print("----------------------")
  print(f"PRODUCTS BELOW MAX PRICE: {max_price}")
  print("----------------------")
  for item, price in products.items():
    if price < max_price:
      print(item, price)
  print("----------------------")

  return

product_filtering()