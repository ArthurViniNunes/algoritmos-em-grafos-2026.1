from collections import deque


def busca_em_largura(grafo):
    visitados = set()
    ordem_visita = []

    for vertice_inicial in grafo:
        if vertice_inicial not in visitados:

            fila = deque([vertice_inicial])
            visitados.add(vertice_inicial)

            while fila:
                vertice_atual = fila.popleft()
                ordem_visita.append(vertice_atual)

                for vizinho in grafo.get(vertice_atual, []):
                    if vizinho not in visitados:
                        visitados.add(vizinho)
                        fila.append(vizinho)

    return ordem_visita


grafo = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B", "D"],
    "E": ["F"],
    "F": ["E"],
    "G": []
}


resultado = busca_em_largura(grafo)

print("Ordem da busca:", resultado)