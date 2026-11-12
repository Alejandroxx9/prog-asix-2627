import math

temps = float(input("Temps d'exercici: "))
litres_a_beure = temps * 0.5
litres_sencers = math.floor(litres_a_beure)

text_hores = "hores"
if temps == 1:
  text_hores = "hora"

text_litres = "litres"
if litres_sencers == 1:
  text_litres = "litre"

print (f"Com has estat, {temps, text_hores}, fent exercici, has de beure {text_litres, litres_a_beure}")