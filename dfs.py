

def dfs(grafo, inicio, fin):
    frontera = [inicio]
    explorados = set()
    padre = {inicio: None}

    while frontera:
        nodo = frontera.pop()   

        if nodo == fin:
            
            camino = []
            while nodo is not None:
                camino.append(nodo)
                nodo = padre[nodo]
            return camino[::-1], len(explorados)

        if nodo not in explorados:
            explorados.add(nodo)

            for vecino in grafo[nodo]:
                if vecino not in explorados:
                    padre[vecino] = nodo
                    frontera.append(vecino)

    return None, len(explorados)
