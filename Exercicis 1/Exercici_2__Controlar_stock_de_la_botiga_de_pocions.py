stock_inicial_inici = int(input("Stock inicial de pocions?: "))
stock_final = stock_inicial_inici


client1 = int(input("Unitats que vols, C1?: "))
stock_final = (stock_final - client1)
print(f"Despres de la compra del client1 ara queden {stock_final}")


client2 = int(input("Unitats que vols, C2?: "))
stock_final = (stock_final - client2)
print(f"Despres de la compra del client2 ara queden {stock_final}")


client3 = int(input("Unitats que vols, C3?: "))
stock_final = (stock_final - client3)
print(f"Despres de la compra del client3 ara queden {stock_final}")


print (f"Stock inicial: {stock_inicial_inici}")
print ("------------------------")
print (f"Compra client 1: -{client1}")
print (f"Compra client 2: -{client2}")
print (f"Compra client 3: -{client3}")
print("------------------------")
print(f"Stock al final del dia: {stock_final} pocions")