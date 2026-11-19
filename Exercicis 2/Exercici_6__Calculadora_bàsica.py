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
    else:
        n1 = float(n1)
        n2 = float(n2)

        if operacio == "+":
            resultat = n1 + n2
            if resultat.is_integer():
                #No tiene decimales
                resultat = round(resultat)
            else:
                print(f"El resultat de {n1} + {n2} és: {resultat}")
                #Tiene decimales
            
        elif operacio == "-":
            resultat = n1 - n2
            if resultat.is_integer():
                #No tiene decimales
                resultat = round(resultat)
            else:
                print(f"El resultat de {n1} - {n2} és: {resultat}")
                #Tiene decimales
                
        elif operacio == "*":
            resultat = n1 * n2
            if resultat.is_integer():
                #No tiene decimales
                resultat = round(resultat)
            else:
                print(f"El resultat de {n1} * {n2} és: {resultat}")
        elif operacio == "/":
            resultat = n1 / n2
            if resultat.is_integer():
                #No tiene decimales
                resultat = round(resultat)
            else:
                print(f"El resultat de {n1} / {n2} és: {resultat}")

print ("ADEU")