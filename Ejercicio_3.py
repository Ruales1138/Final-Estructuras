# Lista de adyacencia G1
lista_g1 = {
  'A': ['B', 'K'],
  'B': ['A', 'K'],
  'C': ['D', 'E', 'K'],
  'D': ['C'],
  'E': ['D'],
  'F': ['C', 'G', 'H', 'I'],
  'G': [],
  'H': [],
  'I': ['J'],
  'J': ['A', 'E'],
  'K': ['C', 'D']
    }

G = { 
0: [1, 2], 
1: [3], 
2: [], 
3: [], 
4: [3] 
} 

class Ejercicio3:
    def __init__(self, lista):
        self.lista = lista

    def GE(self, nodo):
        contador = 0
        for n in self.lista:
            if nodo in self.lista[n]:
                contador += 1
        return contador
    
    def grado_1(self):
        lista_filtrada = []
        for n in self.lista:
            grado = self.GE(n)
            if grado == 1:
                lista_filtrada.append(n)
        return lista_filtrada
    
    def eliminar(self, nodo):
        self.lista.pop(nodo)
        for n in self.lista:
            if nodo in self.lista[n]:
                self.lista[n].remove(nodo)

    def eliminar_grado_1(self):
        lista_filtrada = self.grado_1()
        for n in lista_filtrada:
            self.eliminar(n)

    def __repr__(self):
        return f'{self.lista}'
    

e3 = Ejercicio3(lista_g1)
print(e3)
e3.eliminar_grado_1()
print(e3)