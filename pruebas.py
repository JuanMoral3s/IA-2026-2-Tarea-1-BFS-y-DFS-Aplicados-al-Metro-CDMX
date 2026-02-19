import bfs
import dfs
import grafoMetro
import networkx as nx
import matplotlib.pyplot as plt
import random

def pruebas(inicio, fin):

    # BFS
    rutaBFS, visitados_bfs = bfs.bfs(grafoMetro.metro, inicio, fin)
    print(f"\nResultados BFS desde {inicio} hasta {fin}:")
    if rutaBFS:
        print(" -> ".join(rutaBFS))
        print(f"Saltos: {len(rutaBFS) - 1}")
        print(f"Nodos expandidos: {visitados_bfs}")
    else:
        print("No se encontró ruta")

    # DFS
    rutaDFS, visitados_dfs = dfs.dfs(grafoMetro.metro, inicio, fin)
    print(f"\nResultados DFS desde {inicio} hasta {fin}:")
    if rutaDFS:
        print(" -> ".join(rutaDFS))
        print(f"Saltos: {len(rutaDFS) - 1}")
        print(f"Nodos expandidos: {visitados_dfs}")
    else:
        print("No hay una ruta")

    
    graficarRutas(grafoMetro.metro, rutaBFS, rutaDFS, inicio, fin)


def pruebasSinGraficar(inicio, fin):

    # BFS
    rutaBFS, visitados_bfs = bfs.bfs(grafoMetro.metro, inicio, fin)

    # DFS
    rutaDFS, visitados_dfs = dfs.dfs(grafoMetro.metro, inicio, fin)
    
    if rutaBFS is not None and rutaDFS is not None:
        return True
    
    return False


def graficarRutas(mapaMetro, rutaBFS, rutaDFS, inicio, fin):

    G = nx.Graph()
    for estacion, vecinos in mapaMetro.items():
        for v in vecinos:
            G.add_edge(estacion, v)

    
    pos = nx.kamada_kawai_layout(G)

    fig, axes = plt.subplots(1, 2, figsize=(20, 10))

    # BFS 
    ax = axes[0]
    ax.set_title(f"BFS: {inicio} -> {fin}")

    nx.draw_networkx_edges(G, pos, ax=ax, width=0.3, alpha=0.3)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=15)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=5)

    if rutaBFS:
        edges_bfs = [(rutaBFS[i], rutaBFS[i+1]) for i in range(len(rutaBFS)-1)]
        nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edges_bfs, width=2, edge_color= "red")

    # DFS 
    ax = axes[1]
    ax.set_title(f"DFS: {inicio} -> {fin}")

    nx.draw_networkx_edges(G, pos, ax=ax, width=0.3, alpha=0.3)
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=15)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=5)

    if rutaDFS:
        edges_dfs = [(rutaDFS[i], rutaDFS[i+1]) for i in range(len(rutaDFS)-1)]
        nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edges_dfs, width=2, edge_color="blue")

    plt.tight_layout()
    plt.show()

import random

def estacionesAleatorias():
    estaciones = list(grafoMetro.metro.keys())
    inicio, fin = random.sample(estaciones, 2)
    return inicio, fin

