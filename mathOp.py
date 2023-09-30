def add_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Error")
    result = []
    for i in range(len(array1)):
        result.append(array1[i] + array2[i])
    return tuple(result)

def multiply_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Error")
    result = []
    for i in range(len(array1)):
        result.append(array1[i] * array2[i])
    return tuple(result)

def matriz_transpuesta(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

def matriz_adjunta(matriz):
    adjunta = []
    for i in range(len(matriz)):
        filaAdjunta = []
        for j in range(len(matriz)):
            submatriz = [fila[:j] + fila[j+1:] for fila in (matriz[:i]+matriz[i+1:])]
            cofactor = ((-1)**(i+j)) * determinante(submatriz)
            filaAdjunta.append(cofactor)
        adjunta.append(filaAdjunta)
    return matriz_transpuesta(adjunta)

def multiplicar_matrices(matriz1, matriz2):
    filasMatriz1 = len(matriz1)
    columnasMatriz1 = len(matriz1[0])
    filasMatriz2 = len(matriz2)
    columnasMatriz2 = len(matriz2[0])
    if columnasMatriz1 != filasMatriz2:
        print("Error")
        return None
    matrizResultado = [[0 for y in range(columnasMatriz2)] for x in range(filasMatriz1)]
    for i in range(filasMatriz1):
        for j in range(columnasMatriz2):
            for k in range(columnasMatriz1):
                matrizResultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return matrizResultado

def determinante(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    det = 0
    for i in range(len(matriz)):
        submatriz = [fila[1:] for fila in matriz[:i] + matriz[i+1:]]
        det += ((-1)**i) * matriz[i][0] * determinante(submatriz)
    return det

def multiplicar_matriz_vector(matriz,vector):
    filasMatriz = len(matriz)
    columnasMatriz = len(matriz[0])
    filasVector = len(vector)
    if columnasMatriz!= filasVector:
        print("Error")
        return None
    vectorResultado = [0 for x in range(filasMatriz)]
    for i in range(filasMatriz):
        for k in range(columnasMatriz):
            vectorResultado[i] += matriz[i][k] * vector[k]
    return vectorResultado

def matriz_inversa(matriz):
    det = determinante(matriz)
    if det == 0:
        raise ValueError("Error")
    adjunta = matriz_adjunta(matriz)
    inversa = [[adjunta[i][j] / det for j in range(len(adjunta))] for i in range(len(adjunta))]
    return inversa


def producto_cruz(vector1, vector2):
    if len(vector1) != 3 or len(vector2) != 3:
        raise ValueError("Error")
    a1, a2, a3 = vector1
    b1, b2, b3 = vector2
    productoCruzX = a2 * b3 - a3 * b2
    productoCruzY = a3 * b1 - a1 * b3
    productoCruzZ = a1 * b2 - a2 * b1
    return (productoCruzX, productoCruzY, productoCruzZ)


def subtract_arrays(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("Error")
    result = []
    for i in range(len(array1)):
        result.append(array1[i] - array2[i])
    return tuple(result)

def multiply_scalar_array(scalar, array):
    result = []
    for i in range(len(array)):
        result.append(scalar * array[i])
    return tuple(result)

def divide_array_scalar(array,scalar):
    result = []
    for i in range(len(array)):
        result.append(array[i]/scalar)
    return tuple(result)

def calcular_norma(vector):
    sumaCuadrados = sum(componente ** 2 for componente in vector)
    norma = sumaCuadrados ** 0.5
    return norma

def normalizar_vector(vector):
    norma = calcular_norma(vector)
    if norma == 0:
        raise ValueError("Error")
    vectorNormalizado = [componente/norma for componente in vector]
    return tuple(vectorNormalizado)


def producto_punto(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Error")
    product = sum(x * y for x, y in zip(vector1, vector2))
    return product

def deny_array(vector):
    vector = list(vector)
    for i in range(len(vector)):
        vector[i] *= -1    
    return vector