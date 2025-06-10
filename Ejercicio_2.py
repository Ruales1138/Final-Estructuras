G1 = [
  [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
  [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
  [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
]
nodos_g1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

G = [ 
[-1, 1, 2, -1], 
[-1, -1, -1, 2], 
[-1, -1, -1, 3], 
[-1, -1, -1, -1] 
] 
V = [0,1,2,3] 
u = 0 
v = 3 
W = 5

class Ejercicio2:
    def __init__(self, matriz, valores):
        self.matriz = matriz
        self.valores = valores

    def buscar_caminos(self, inicio, final, current = None, visitados = []):
        if inicio not in self.valores or final not in self.valores:
            return []
        if current is None:
            current = inicio
        if visitados == []:
            visitados.append(current)
        if current == final:
            print('aquita')
            return
        pos_current = self.valores.index(current)
        vecinos = self.matriz[pos_current]
        print(vecinos)
        for i, valor in enumerate(vecinos):
            if valor == 0:
                continue
            visitados.append(self.valores[i])
            self.buscar_caminos(inicio, final, self.valores[i], visitados)
        return visitados

        

    

e2 = Ejercicio2(G1, nodos_g1)
print(e2.buscar_caminos('A', 'C'))