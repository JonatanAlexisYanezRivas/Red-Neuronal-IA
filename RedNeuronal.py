from math import exp
import numpy as np

class Red:
    def __init__(self):
        self.numNodos = int(input("Ingrese numero de nodos: "))
        self.out = None
        self.bias = None
        self.pesos = None
        
RNA = []

def generarOut(t):
    global RNA
    matriz = []
    if(t == 0):
        for i in range(RNA[t].numNodos):
            entrada = int(input(f"ingrese x{i}: "))
            matriz.append(entrada)
        return np.array(matriz).reshape(RNA[t].numNodos,1)
    

def generarBias(t):
    global RNA
    if(t != 0):     
        return np.random.uniform(0,1, size=(RNA[t].numNodos,1))

def generarPesos(t):
    global RNA
    if(t != 0):
        return np.random.uniform(-2,2, size=(RNA[t].numNodos,RNA[t - 1].numNodos))

def calcularSalidas(t):
    global RNA
    salidas = []
    if( t != 0):
        array =  np.dot(RNA[t].pesos, RNA[t - 1].out)
        suma = array + RNA[t].bias
        for i in range(RNA[t].numNodos):
            salidas.append(1/(1 + exp((-0.5)*suma[i])))
        return np.array(salidas).reshape(RNA[t].numNodos,1)
    else:
        return RNA[0].out

def calcularError(t):
    error = []
    suma = 0
    salidas = RNA[t].out
    for i in range(RNA[t].numNodos):
        error.append(int(input(f"ingrese valor esperado(t{i}): ")) - salidas[i])
    for j in range(RNA[t].numNodos):
        suma = suma + pow(error[j],2)
    print(f"Error total: {suma}")
    
tamanio = int(input("ingrese tamaño(número de capas de la red): "))

for i in range(tamanio):
    if(i == 0):
        print("\n***capa de entrada***")
        RNA.append(Red())
        RNA[0].out = generarOut(0)
    elif(i < tamanio-1):
        print(f"\n***Capa: {i} ***")
        RNA.append(Red())
        print(f"------------matriz bias {i}----------")
        RNA[i].bias = generarBias(i)
        print(RNA[i].bias)
        print(f"------------matriz pesos {i}----------")
        RNA[i].pesos = generarPesos(i)
        print(RNA[i].pesos)
        print(f"-------matriz salidas  {i}-------")
        RNA[i].out = calcularSalidas(i)
        print(RNA[i].out)
    elif(i == tamanio - 1):
        print("\n***capa de salidad***")
        RNA.append(Red())
        print(f"------------matriz bias {i}----------")
        RNA[i].bias = generarBias(i)
        print(RNA[i].bias)
        print(f"------------matriz pesos {i}----------")
        RNA[i].pesos = generarPesos(i)
        print(RNA[i].pesos)
        print(f"-------matriz salidas  {i}-------")
        RNA[i].out = calcularSalidas(i)
        print(RNA[i].out)

print("\n***Error***")
calcularError(tamanio - 1)