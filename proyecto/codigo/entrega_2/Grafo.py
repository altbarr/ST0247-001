import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from collections import deque
direccion_de_mapa_acoso = 'https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/calles_de_medellin_con_acoso.csv'

calles_de_medellin = pd.read_csv(direccion_de_mapa_acoso, sep=';')
#print(calles_de_medellin)

dirección_mapa_poligono = 'https://raw.githubusercontent.com/mauriciotoro/ST0245-Eafit/master/proyecto/Datasets/poligono_de_medellin.csv'
area_de_medellin = pd.read_csv(dirección_mapa_poligono, sep=';')
#print(mapa_poligono)
calles_de_medellin.head(50)

verticesNoDirigidos = calles_de_medellin[calles_de_medellin['oneway'] == False]

verticesDirigidos = calles_de_medellin[calles_de_medellin['oneway'] == True]

class Grafo():
    def __init__(self):       
        self.vertexList = []
        self.edgeList = []
    
    def addVertex(self, vertex):
        #Lista con el vertice y las conexiones del vertice
        #Las conexiones serán diccionarios con los siguientes datos
        #->VerticeDestino
        #->Distancia
        #->Riesgo
        self.vertexList.append(vertex)
        self.edgeList.append([])
    
    def addEdge(self, source, destination, length, risk, name = None):
        index = self.vertexList.index(source)
        if not (index == -1):
            self.edgeList[index].append({'destination' : destination,
                                               'length' : length,
                                               'risk' : risk,
                                               'name' : name})
    
    def addEdgeNoDirected(self, vertex1, vertex2, length, risk, name = None):
        self.addEdge(vertex1, vertex2, length, risk, name)
        self.addEdge(vertex2, vertex1, length, risk, name)
    
    def getEdge(self, source, destination):
        index = self.vertexList.index(source)
        listEdge =list(filter(lambda edge: edge['destination'] == destination, 
                              self.edgeList[index]))
        return listEdge[0]
    def getRisk(self, source, destination):
        attributes = self.getEdge(source, destination)
        return attributes['risk']
    
    def getLength(self, source, destination):
        attributes = self.getEdge(source, destination)
        return attributes['length']
    
    def getVertexes(self):
        vertexList = []
        for vertex in self.vertexList:
            vertexList.append(vertex)
        return vertexList
    
    def getEdges(self):
        return self.edgeList
    def getGraph(self):
        allList = []
        i = 0
        for vertice in self.vertexList:
            allList.append(i)
            allList.append(self.edgeList[i])
            i+=1
            
            
 vertexDuplicados = np.concatenate((calles_de_medellin['origin'], calles_de_medellin['destination']))
vertex = np.unique(vertexDuplicados)
print(np.count_nonzero(vertex))
print(vertex)

grafo = Grafo()
for vertice in vertex:
    grafo.addVertex(vertice)
    
originNum = 2
destinationNum = 3
lengthNum = 4
riskNum = 6
nameNum = 1

for vertice in verticesDirigidos.itertuples():
    grafo.addEdge(vertice[originNum], 
                  vertice[destinationNum], 
                  vertice[lengthNum],
                  vertice[riskNum],
                  vertice[nameNum])
    
 for vertice in verticesNoDirigidos.itertuples():
    grafo.addEdgeNoDirected(vertice[originNum], 
                  vertice[destinationNum], 
                  vertice[lengthNum],
                  vertice[riskNum],
                  vertice[nameNum])
    
    #https://colab.research.google.com/drive/1FRRW1t73nejaCuqVFq22Mz0x5_NigmYx?usp=sharing#scrollTo=c2ZGGkx5psQD
