print ("Calculadora Bàsica")
print (42*"=")

operacio=input("Introdueix l'operació que vols realitzar (+, -, *, /): ")

if operacio not in ["+", "-", "*", "/"]:
    print("Operació no vàlida. Si us plau, introdueix una operació vàlida.")
else:
    n1 = input("Introdueix el primer número: ")
    n2 = input("Introdueix el segon número: ")

    if not n1.isnumeric() or not n2.isnumeric():
        print("Si us plau, introdueix només números vàlids.")

print ("ADEU")