a = int(input("Introdueix el número A: "))
b = int(input("Introdueix el número B: "))

print("-"*42)
if a > b:
  print(f"{a} es més gran que {b}")

elif a < b:
  print(f"{a} es més petita que {b}")

elif a == b:
  print(f"{a} es igual que {b}")
print("-"*42)