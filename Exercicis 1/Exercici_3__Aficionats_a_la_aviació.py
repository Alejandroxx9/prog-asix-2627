nusos = float(input("Velocitat en nusos: "))
minuts = float(input("Temps de vol en minuts: "))

distancia = nusos * 1.852 * minuts / 60

print(f"La nostra aeronau ha viatjat durant {minuts} a {nusos} nusos, de manera que ha recorregut {distancia} Km")