import math

litres_aigua = float(0.5)
hores_ciclisme = int(input("Quantes hores has fet exercici?: "))
total_a_beure = (litres_aigua * hores_ciclisme)
total = math.floor(total_a_beure)
if hores_ciclisme == 1:
  print(f"Com has estat {hores_ciclisme} hora fent exercici, has de beure {total} litres de líquid per mantenir-te en un bon nivell d'hidratació")
elif hores_ciclisme == 2:
  print(f"Com has estat {hores_ciclisme} hores fent exercici, has de beure {total} litre de líquid per mantenir-te en un bon nivell d'hidratació")
elif hores_ciclisme == 3:
  print(f"Com has estat {hores_ciclisme} hores fent exercici, has de beure {total} litre de líquid per mantenir-te en un bon nivell d'hidratació")
else:
  print(f"Com has estat {hores_ciclisme} hores fent exercici, has de beure {total} litres de líquid per mantenir-te en un bon nivell d'hidratació")