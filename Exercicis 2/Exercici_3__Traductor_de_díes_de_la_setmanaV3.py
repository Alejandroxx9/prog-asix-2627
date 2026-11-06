raza = input("Es vosté Interiá (I) o Stringeriá (S)?: ")
if raza == "I":
  dia_setmana_I=input("Dia de la setmana: ")
  match dia_setmana_I:
    case "Dilluns":
      print("Traducció: 1")
    case "Dimarts":
      print("Traducció: 2")
    case "Dimecres":
      print("Traducció: 3")
    case "Dijous":
      print("Traducció: 4")
    case "Divendres":
      print("Traducció: 5")
    case "Dissabte":
      print("Traducció: 6")
    case "Diumenge":
      print("Traducció: 7")
elif raza == "S":
  dia_setmana_S=int(input("Dia de la setmana: "))
  match dia_setmana_S:
    case 1:
      print("Traducció: Dilluns")
    case 2:
      print("Traducció: Dimarts")
    case 3:
      print("Traducció: Dimecres")
    case 4:
      print("Traducció: Dijous")
    case 5:
      print("Traducció: Divendres")
    case 6:
      print("Traducció: Dissabte")
    case 7:
      print("Traducció: Diumenge")