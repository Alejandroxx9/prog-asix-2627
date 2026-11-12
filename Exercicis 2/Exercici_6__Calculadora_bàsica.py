print ("Calculadora Bàsica")
print (42*"=")

calc = input("Introdueix operació a realitzar (+,-,*,/): ")
if calc not in ("+,-,*,/"):
    calc = print(f"Simbol equivocat")
else:
    n1 = int(input("Introudeix el primer nº: "))
    n2 = int(input("Introudeix el segon nº: "))
    if calc == "+":
        print(f"{n1} + {n2} = {n1+n2}")
    elif calc == "-":
        print(f"{n1} - {n2} = {n1-n2}")
    elif calc == "*":
        print(f"{n1} * {n2} = {n1*n2}")
    elif calc == "/":
        print(f"{n1} / {n2} = {n1/n2}")