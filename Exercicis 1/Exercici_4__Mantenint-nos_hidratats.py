import math

litres_aigua = float(0.5)
hores_ciclisme = int(input("Quantes hores has fet exercici?: "))
total_a_beure = (litres_aigua * hores_ciclisme)
total = math.floor(total_a_beure)

print(f"Com has estat {hores_ciclisme} fent exercici, has de beure {total} litre de líquid per mantenir-te en un bon nivell d'hidratació")