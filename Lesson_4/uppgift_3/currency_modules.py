"""Skapa en modul som innehåller funktioner för att omvandla svenska kronor till
tre andra valutor (USD, EUR, GBP). Använd fasta växelkurser
"""

def sek_to_USD(sek:float):
  #1 sek = 0,098 USD
  usd = sek*0.098
  return usd
  
def sek_to_EUR(sek:float):
  #1 sek = 0,088 Euro
  eur = sek*0.088
  return eur
  
def sek_to_GBP(sek:float):
   #1 sek = 0,074 Pound sterling
   gbp = sek*0.074
   return gbp


  