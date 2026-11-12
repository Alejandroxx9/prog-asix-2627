stock_inicial = int(input("Stock inicial de pocions: "))

cli1 = int(input("Compra client 1: "))
if cli1 >= stock_inicial:
    print(f"No pots comprar més de {stock_inicial} pocions, per tant et venem el que queda")
else:
    stock_final = (stock_inicial - cli1)
    cli2 = int(input("Compra client 2: "))
    if cli2 >= stock_final:
        print(f"No pots comprar més de {stock_final} pocions, per tant et venem el que queda")
    else:
        stock_final = (stock_final - cli2)
    
    cli3 = int(input("Compra client 3: "))
    if cli3 >= stock_final:
        print(f"El Client 3 ha comprat totes les {stock_final} pocions disponibles")
    else:
        stock_final = (stock_final - cli3)
        print(f"Stock inicial: {stock_inicial}")
        print(f"Compra client 1: {cli1}")
        print(f"Compra client 2: {cli2}")
        print(f"Compra client 3: {cli3}")
        print(f"Stock al final del dia: {stock_final}")