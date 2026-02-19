from collections import deque

def bfs(grafo, inicio, fin):
    frontera = deque([inicio])
    explorados = set()
    padre = {inicio: None}

    while frontera:
        nodo = frontera.popleft()

        if nodo == fin:
            
            camino = []
            while nodo is not None:
                camino.append(nodo)
                nodo = padre[nodo]
            return camino[::-1],len(explorados)
        
        explorados.add(nodo)

        for vecino in grafo[nodo]:
            if vecino not in explorados and vecino not in frontera:
                padre[vecino] = nodo
                frontera.append(vecino)
        
    return None, len(explorados)

