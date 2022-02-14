class Grafo(object):
    def __init__(self):
        self.relaciones = {}
    def __str__(self):
            return str(self.relaciones)
    
def agregar(grafo, elemento):
    grafo.relaciones.update({elemento:[]})

def relacionar(grafo, elemento1, elemento2):
    relacionarUnilateral(grafo, elemento2, elemento1)
    relacionarUnilateral(grafo, elemento1, elemento2)
    
def relacionarUnilateral(grafo, origen, destino):
    grafo.relaciones[origen].append(destino)
        
def evaluarColores(g):
    num = [0]
    primerColor = []
    segundoColor = []
    recorrerGrafo(g, "0", primerColor, segundoColor, num)
    print(set(primerColor))
    print(set(segundoColor))
    return bool(set(primerColor).intersection(segundoColor))
    
def recorrerGrafo(grafo, elementoInicial, pC, sC, n, elementosRecorridos = []):
    if elementoInicial in elementosRecorridos:
        return
    asignarColor(elementoInicial, pC, sC, n)
    elementosRecorridos.append(elementoInicial)
    for vecino in grafo.relaciones[elementoInicial]:

        if elementoInicial in pC:
            if vecino in pC:
                sC.append(vecino)
        elif elementoInicial in sC:
            if vecino in sC:
                pC.append(vecino)

        if elementoInicial in pC:
            n[0] = 1
        elif elementoInicial in sC:
            n[0] = 0
        recorrerGrafo(grafo, vecino, pC, sC, n, elementosRecorridos)
    
def asignarColor(elemento, primerColor, segundoColor, numero):
    if (numero[0] % 2) == 0 and not numero[0] == 1:
        primerColor.append(elemento)
    else:
        segundoColor.append(elemento)
        
print("Ingrese la cantidad de nodos")
nodos = int(input())
"""
if nodos == 0:
    break
"""
print("Ingrese la cantidad de arcos ")
arcos = int(input())

grafo = Grafo()
for i in range(0, nodos):
    agregar(grafo, str(i))
print("Ingrese las relaciones")
for i in range(0, arcos):
    relacion = input()
    primerElemento = relacion[0]
    segundoElemento = relacion[2]
    relacionar(grafo, primerElemento, segundoElemento)
if(not evaluarColores(grafo)):
    print("Bicoloreable")
else:
    print("Not Bicoloreable")