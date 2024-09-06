import currency_modules
"""
Skapa ett huvudprogram där användaren får mata in ett belopp i SEK och välja
till vilken valuta de vill omvandla.
"""

def currency_converter():
  sek = float(input("Please enter the amount you wish to convert (SEK)\n"))
  user_option = int(input("Please select the currency you wish to convert you money to:\n1) USD\n2) GPB\n3) EUR\n4) Quit program\n"))
  while user_option != 4:
    if user_option == 1:
      print(currency_modules.sek_to_USD(sek))      

    elif user_option == 2:
      print(currency_modules.sek_to_GBP(sek))   
      
    elif user_option == 3:
      print(currency_modules.sek_to_EUR(sek))

    elif user_option == 4:
      print("Closing program")
      break

    user_option = int(input("Please select the currency you wish to convert you money to:\n1) USD\n2) GPB\n3) EUR\n4) Quit program\n"))

currency_converter()


