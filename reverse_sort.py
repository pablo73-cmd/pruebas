
n = int(input("¿Cuántos elementos tendrá el vector? "))


vector = []


for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i+1}: "))
    vector.append(elemento)


vector.sort(reverse=True)


print("Vector ordenado (inverso):", vector)
