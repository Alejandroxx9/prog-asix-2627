print ("Calculadora Bàsica")
print (42*"=")

operacio=input("Introdueix l'operació que vols realitzar (+, -, *, /): ")

if operacio not in ["+", "-", "*", "/"]:
    print("Operació no vàlida. Si us plau, introdueix una operació vàlida.")

else:
    n1 = input("Introdueix el primer número: ")
    n2 = input("Introdueix el segon número: ")
    
    #COMPROBACIONES
    if not isinstance(n1, (float, int)) or not isinstance(n2, (float, int)):
        print("Si us plau, introdueix només números vàlids.")

    
    else:
        n1 = float(n1)
        n2 = float(n2)

        if operacio == "+":
            resultat = n1 + n2
            print(f"El resultat de {n1} + {n2} és: {resultat}")
        elif operacio == "-":
            resultat = n1 - n2
            print(f"El resultat de {n1} - {n2} és: {resultat}")
        elif operacio == "*":
            resultat = n1 * n2
            print(f"El resultat de {n1} * {n2} és: {resultat}")
        elif operacio == "/":
            if n2 == 0:
                print("Error: No es pot dividir per zero.")
            else:
                resultat = n1 / n2
                print(f"El resultat de {n1} / {n2} és: {resultat}")

print ("ADEU")