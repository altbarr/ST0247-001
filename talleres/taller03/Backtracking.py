def hallarPen(x1,x2,y1,y2):
    m = abs((y2-y1)/(x2-x1))
    if m == 1 or m == 0:
        return True
    return False
    
def atacarHastaI(tablero, i):
    for j in range(0,i+1):
        for k in range(j+1,i+1):
            if hallarPen(j,k,tablero[j],tablero[k]) == True:
                return True
    return False

def nreinas(n):
    l = []
    nReinasAux(n, 0, [0]*n, l)
    return l

def nReinasAux(numero, casilla, tablero, lista):
    if casilla == numero:
        lista.append(list(tablero))
        return
    for f in range(numero):
        tablero[casilla] = f
        if not atacarHastaI(tablero, casilla):
            nReinasAux(numero, casilla+1, tablero, lista)
print(nreinas(4))