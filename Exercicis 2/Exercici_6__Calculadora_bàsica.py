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

    #CONVERTIMOS LOS NUMEROS INTEGROS A NUMEROS FLOAT
    else:
        n1 = float(n1)
        n2 = float(n2)
        
        #SUMA
        if operacio == "+":
            resultat = n1 + n2
            print(f"El resultat de {n1} + {n2} és: {resultat}")
            
        #RESTA 
        elif operacio == "-":
            resultat = n1 - n2
            print(f"El resultat de {n1} - {n2} és: {resultat}")
            
        #MULTIPLICACION
        elif operacio == "*":
            resultat = n1 * n2
            print(f"El resultat de {n1} * {n2} és: {resultat}")
            
        #DIVISION
        elif operacio == "/":
            resultat = n1 / n2
            print(f"El resultat de {n1} / {n2} és: {resultat}")

print ("ADEU")