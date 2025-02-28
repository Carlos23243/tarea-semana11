def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j) 
    return None  
data = [
    [5, 8, 2],
    [3, 7, 1],
    [6, 4, 9]
]
valor_buscar = int(input("Ingrese el valor a buscar: "))
resultado = buscar_valor(data, valor_buscar)
if resultado:
    print(f"El valor {valor_buscar} se encontró en la posición {resultado} (fila {resultado[0]}, columna {resultado[1]})")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")
