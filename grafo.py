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
    
    def lista_adyacencia(self):
        adyacencia = {nodo: [] for nodo in self.nodos}  
        for arista in self.aristas:
            adyacencia[arista.origen].append((arista.destino, arista.attrs))
            if not self.dirigido:
                adyacencia[arista.destino].append((arista.origen, arista.attrs))
        return adyacencia

    def lista_incidencia(self):
        incidencia = {nodo: [] for nodo in self.nodos}
        for arista in self.aristas:
            incidencia[arista.origen].append(arista)
            if not self.dirigido:
                incidencia[arista.destino].append(arista)
            else:
                incidencia[arista.destino].append(arista)  
        return incidencia
    
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
    
    def matriz_incidencia(self):
        nodos = list(self.nodos.keys())        
        aristas = self.aristas                 
        n = len(nodos)
        m = len(aristas)
        
        idx_nodo = {n: i for i, n in enumerate(nodos)}  
        M = [[0] * m for _ in range(n)]
        
        for j, arista in enumerate(aristas):
            i_origen = idx_nodo[arista.origen]
            i_destino = idx_nodo[arista.destino]
            
            if self.dirigido:
                M[i_origen][j] = -1
                M[i_destino][j] = 1
            else:
                M[i_origen][j] = 1
                M[i_destino][j] = 1
        return M, nodos, aristas


def menu():
    print("\n--- Menu ---")
    print("1. Crear grafo dirigido")
    print("2. Crear grafo no dirigido")
    print("3. Agregar nodo")
    print("4. Agregar arista")
    print("5. Mostrar lista de adyacencia")
    print("6. Mostrar lista de incidencia")
    print("7. Mostrar matriz de adyacencia")
    print("8. Mostrar matriz de incidencia")
    print("9. Salir")

grafo = None

while True:
    menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        grafo = Grafo(dirigido=True)
        print("Grafo dirigido creado.")
    elif opcion == "2":
        grafo = Grafo(dirigido=False)
        print("Grafo no dirigido creado.")
    elif opcion == "3":
        if grafo:
            nodo = input("Ingrese el id del nodo: ")
            grafo.agregar_nodo(nodo)
            print(f"Nodo {nodo} agregado.")
        else:
            print("Primero cree un grafo.")
    elif opcion == "4":
        if grafo:
            origen = input("Ingrese nodo origen: ")
            destino = input("Ingrese nodo destino: ")
            peso = input("Ingrese peso (opcional, ENTER si no): ")
            attrs = {"Peso": int(peso)} if peso else {}
            grafo.agregar_arista(origen, destino, attrs)
            print(f"Arista {origen} -> {destino} agregada.")
        else:
            print("Primero cree un grafo.")
    elif opcion == "5":
        if grafo:
            print("\nLista de adyacencia:")
            print(grafo.lista_adyacencia())
        else:
            print("Primero cree un grafo.")
    elif opcion == "6":
        if grafo:
            print("\nLista de incidencia:")
            print(grafo.lista_incidencia())
        else:
            print("Primero cree un grafo.")
    elif opcion == "7":
        if grafo:
            M, nodos = grafo.matriz_adyacencia()
            print("\nMatriz de adyacencia:")
            print("   " + "  ".join(nodos))
            for i, fila in enumerate(M):
                print(f"{nodos[i]} {fila}")
        else:
            print("Primero cree un grafo.")
    elif opcion == "8":
        if grafo:
            Mi, nodos, aristas = grafo.matriz_incidencia()
            print("\nMatriz de incidencia:")
            print("       " + "  ".join([f"e{j}" for j in range(len(aristas))]))
            for i, fila in enumerate(Mi):
                print(f"{nodos[i]}  {fila}")
        else:
            print("Primero cree un grafo.")
    elif opcion == "9":
        print("Saliendo...")
        break
    else:
        print("Opcion invalida.")
