# Solicitando elementos de List/Set uno por uno.

List = list()
Set = set()

l = int(input("Introduzca el tamaño de la lista: "))
s = int(input("Introduzca el tamaño del set: "))

print("Introduzca los elementos de la lista:")
for i in range(l):
    List.append(int(input(f"Elemento {i+1}: ")))

print("Introduzca los elementos del set:")
for i in range(s):
    Set.add(int(input(f"Elemento {i+1}: ")))

print("Lista ingresada:", List)
print("Set ingresado:", Set)


