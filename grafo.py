from node import Nodo
from arista import Arista

class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.nodos = {}   
        self.aristas = [] 

    def agregar_nodo(self, id, attrs=None):
        if id not in self.nodos:
            self.nodos[id] = Nodo(id, attrs)
        return self.nodos[id]

    def agregar_arista(self, origen, destino, attrs=None):
        if origen not in self.nodos:
            self.agregar_nodo(origen)
        if destino not in self.nodos:
            self.agregar_nodo(destino)

        arista = Arista(origen, destino, attrs, dirigida=self.dirigido)
        self.aristas.append(arista)
        return arista

    def __repr__(self):
        tipo = "Dirigido" if self.dirigido else "No dirigido"
        return f"<Grafo {tipo}: {len(self.nodos)} nodos, {len(self.aristas)} aristas>"


    def matriz_adyacencia(self):
       
        nodos = list(self.nodos.keys())             
        idx = {n: i for i, n in enumerate(nodos)}  
        n = len(nodos)
        M = [[0] * n for _ in range(n)]              

        for a in self.aristas:
            i = idx[a.origen]
            j = idx[a.destino]
            M[i][j] = 1
            if not self.dirigido:
                M[j][i] = 1

        return M, nodos
    
    
    def lista_incidencia(self):
        incidencia = {nodo: [] for nodo in self.nodos}  
        for arista in self.aristas:
            incidencia[arista.origen].append((arista.destino, arista.attrs))
            if not self.dirigido:
                incidencia[arista.destino].append((arista.origen, arista.attrs))

        return incidencia


k2 = Grafo(dirigido=True)
k2.agregar_nodo("M1")
k2.agregar_nodo("M2")
k2.agregar_arista("M1", "M2", {"Peso": 5})
k2.agregar_nodo("M3")
k2.agregar_arista("M2","M1",{"Peso":5})
print(k2)
print(k2.aristas)

print(k2.lista_incidencia())


#prueba adyacencia
if __name__ == "__main__":
    g = Grafo(dirigido=False)
    g.agregar_nodo("A")
    g.agregar_nodo("B")
    g.agregar_nodo("C")
    g.agregar_arista("A", "B")
    g.agregar_arista("B", "C")

    M, nodos = g.matriz_adyacencia()
    print("Nodos orden:", nodos)
    for fila in M:
        print(fila)
