def nreinas(n : int):
    pos = ""
    for i in range(0, n):
        pos = pos + str(i)
    reinas = permutacionesReina(pos)
    #mostrarLista(reinas)
    mostrarLista(eliminarCruces(reinas))
    
def mostrarLista(lista):
    for elemento in lista:
        print(*elemento)
  
def eliminarCruces(arreglo):
    i = 0
    rango = len(arreglo)
    while i < rango:
        posiciones = arreglo[i]
        j = 0
        while j < len(posiciones)-1 and arreglo.count(posiciones) > 0:
            k = j+1 
            while k < len(posiciones):
                if hallarPen(j, k, int(posiciones[j]), int(posiciones[k])) == 1.0:
                    # print("x = " + str(j)+ " " + (posiciones[j]) + "\nk = " + str(k) + " " + posiciones[k] + "\n")
                    arreglo.remove(posiciones)
                    rango = len(arreglo)
                    i-=1
                    break
                k+=1
            j+=1
        i+=1
    return arreglo
      

def hallarPen(x1,x2,y1,y2):
    m = (y2-y1)/(x2-x1)
    return abs(m)

def permutacionesReina(cadena):
    listaPer = []
    permutacionesReinaAux(cadena, "", listaPer)
    return listaPer
    
def permutacionesReinaAux(pregunta, respuesta, listaPer):
    if len(pregunta)==0:
      listaPer.append(list(respuesta))
    else:
      for i in range(0,len(pregunta)):
        nuevaPregunta = pregunta[0:i]+pregunta[i+1:]
        permutacionesReinaAux(nuevaPregunta , respuesta+pregunta[i], listaPer)
        
def main():
    #subconjuntosDeUna("abc")
    nreinas(11)
main()