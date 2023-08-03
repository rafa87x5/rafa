lista = [4, "hola", 56, "primo", 45, "aha"]
x = 0
for item in lista:
    if (x - 1) < 0:
        print("nada", item, lista[x + 1])
        x += 1
    elif (x + 1) == len(lista):
        print(lista[x-1], item, "nada")
        x += 1
    else:
        print(lista[x-1], item, lista[x+1])
        x += 1


