maxf = 3
maxc = 5
a = [[0.0] * maxc for _ in range(maxf)]

print("LSC 3J")

for f in range(maxf):
    for c in range(maxc):
        print("Ingrese el valor: ")
        a[f][c]=float(input())


print("Los valores del arreglo son los siguientes: ")
for f in range(maxf):
    for c in range(maxc):
        print(a[f][c],end=" ")
        print()