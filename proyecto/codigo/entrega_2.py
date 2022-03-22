import numpy as np
from collections import deque
import math
# This class represents a directed graph
# using adjacency list representation

class GraphAL:
    def _init_(self, size):
      self.arregloDeListas = [0]*size
      self.size = size
        #[size]
        #[ [], [], [], [] , [] ,[] ...]

      for i in range(0, size):
        self.arregloDeListas[i]= deque()
  
        
    def addArc(self, vertex, destination, weight):
       fila = self.arregloDeListas[vertex]
       arco = (destination,weight)
       fila.append(arco)
        
    def getDistance(self, source, dest):   
      for vertex in self.arregloDeListas[source]:
        if vertex[0]==dest:
          return vertex[1]
      return math.inf
        

    def getSuccessors(self, vertice): 
      succesors = []
      for i in self.arregloDeListas[vertice]:
        succesors.append(i[0])
      return succesors

# ---------------------------- Dijkstra ---------------------------------------------------------
def ponderaciones(graph, source, dest): #(distancia, riesgo, vertice al que apunta)
  if source == dest:
    return (0,0,0)
  else:
    return [graph.getDistance(source, dest), 0, 0]
    

def modificar_tabla(graph, tabla, source, succesor, step):
  if tabla[succesor][step] != -1:
    tabla[succesor][step] =  graph.getDistance(source, succesor)
    return succesor 
  


def dijkstra(graph, source, dest):
  tabla = np.zeros((graph.size, graph.size))
  tabla [tabla == 0 ] = math.inf
  camino = [source]
  menor_peso = math.inf
  menor_sucesor = math.inf

  step = 0
  while source != dest: 
    for succesor in graph.getSuccessors(source):
      posible_menor_sucesor = modificar_tabla(graph, tabla, source, succesor, step)
      posible_menor_peso = graph.getDistance(source, posible_menor_sucesor)
      if posible_menor_peso < menor_peso:
        menor_peso = posible_menor_peso
        menor_sucesor = posible_menor_sucesor

    camino.append(menor_sucesor)
    for i in range(step +1, len(tabla)):
      tabla[menor_sucesor][i] = -1

    source = menor_sucesor
    step +=1
    
  print(tabla)
  return camino

  

size = 4
graph_list = GraphAL(size)

graph_list.addArc(0,1,3)
graph_list.addArc(0,2,4)
graph_list.addArc(0,3,10)
graph_list.addArc(1,0,3)
graph_list.addArc(1,3,1)
graph_list.addArc(1,2,6) 
graph_list.addArc(2,1,6)
graph_list.addArc(2,0,4)
graph_list.addArc(2,3,9)
graph_list.addArc(3,2,9)
graph_list.addArc(3,1,1)
graph_list.addArc(3,0,10)

dijkstra(graph_list, 0, 3)import numpy as np
from collections import deque
import math
# This class represents a directed graph
# using adjacency list representation

class GraphAL:
    def _init_(self, size):
      self.arregloDeListas = [0]*size
      self.size = size
        #[size]
        #[ [], [], [], [] , [] ,[] ...]

      for i in range(0, size):
        self.arregloDeListas[i]= deque()
  
        
    def addArc(self, vertex, destination, weight):
       fila = self.arregloDeListas[vertex]
       arco = (destination,weight)
       fila.append(arco)
        
    def getDistance(self, source, dest):   
      for vertex in self.arregloDeListas[source]:
        if vertex[0]==dest:
          return vertex[1]
      return math.inf
        

    def getSuccessors(self, vertice): 
      succesors = []
      for i in self.arregloDeListas[vertice]:
        succesors.append(i[0])
      return succesors

# ---------------------------- Dijkstra ---------------------------------------------------------
def ponderaciones(graph, source, dest): #(distancia, riesgo, vertice al que apunta)
  if source == dest:
    return (0,0,0)
  else:
    return [graph.getDistance(source, dest), 0, 0]
    

def modificar_tabla(graph, tabla, source, succesor, step):
  if tabla[succesor][step] != -1:
    tabla[succesor][step] =  graph.getDistance(source, succesor)
    return succesor 
  


def dijkstra(graph, source, dest):
  tabla = np.zeros((graph.size, graph.size))
  tabla [tabla == 0 ] = math.inf
  camino = [source]
  menor_peso = math.inf
  menor_sucesor = math.inf

  step = 0
  while source != dest: 
    for succesor in graph.getSuccessors(source):
      posible_menor_sucesor = modificar_tabla(graph, tabla, source, succesor, step)
      posible_menor_peso = graph.getDistance(source, posible_menor_sucesor)
      if posible_menor_peso < menor_peso:
        menor_peso = posible_menor_peso
        menor_sucesor = posible_menor_sucesor

    camino.append(menor_sucesor)
    for i in range(step +1, len(tabla)):
      tabla[menor_sucesor][i] = -1

    source = menor_sucesor
    step +=1
    
  print(tabla)
  return camino

  

size = 4
graph_list = GraphAL(size)

graph_list.addArc(0,1,3)
graph_list.addArc(0,2,4)
graph_list.addArc(0,3,10)
graph_list.addArc(1,0,3)
graph_list.addArc(1,3,1)
graph_list.addArc(1,2,6) 
graph_list.addArc(2,1,6)
graph_list.addArc(2,0,4)
graph_list.addArc(2,3,9)
graph_list.addArc(3,2,9)
graph_list.addArc(3,1,1)
graph_list.addArc(3,0,10)

dijkstra(graph_list, 0, 3)
