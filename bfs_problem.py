# Problema: 
# "Há dois tipos de lutadores profissionais: os "bonzinhos" e os "vilões".
# Entre qualquer par de lutadores profissionais pode ou não haver uma rivalidade. 
# Suponha que tenhamos n lutadores profissionais e uma lista de r pares de lutadores entre os quais há rivalidade. 
# Dê um algoritmo que determine se é possível designar alguns dos lutadores como bonzinhos e os restantes como vilões, de modo que a rivalidade ocorra sempre entre um bonzinho e um vilão. 
# Se for possível realizar tal designação, seu algoritmo deve produzi-la."


# Ideia: 
# "Executamos uma BFS para construir uma árvore de busca. 
# Atribuímos cores alternadas aos níveis da árvore. 
# Em seguida, verificamos todas as arestas do grafo. 
# Se alguma aresta conectar dois vértices de mesma cor, a divisão entre bonzinhos e vilões é impossível; caso contrário, a própria coloração obtida fornece a designação."


# Algoritmo:
from collections import deque

def classificar_lutadores(grafo):
    n = len(grafo)

    # Vetor de coloração
    # -1 = ainda não visitado / cinza
    #  0 = bonzinho / azul
    #  1 = vilão / vermelho
    cor = [-1] * n

    for atual in range(n):

        # O grafo pode ser desconexo
        if cor[atual] != -1:
            continue

        fila = deque([atual])
        cor[atual] = 0

        while fila:
            u = fila.popleft()

            for v in range(n):

                # Existe rivalidade entre u e v
                if grafo[u][v] == 1:

                    # Ainda não visitado
                    if cor[v] == -1:
                        cor[v] = 1 - cor[u]
                        fila.append(v)

                    # Os dois têm a mesma cor
                    elif cor[v] == cor[u]:
                        return False, None

    return True, cor



# Rodando um exemplo que funciona:
# Representação do grafo como matriz de adjacência: 4 lutadores, com rivalidades entre (0,1), (0,2), (1,3) e (2,3)

grafo = [
    [0, 1, 1, 0],    #A
    [1, 0, 0, 1],    #B
    [1, 0, 0, 1],    #C
    [0, 1, 1, 0]     #D
]

possivel, designacao = classificar_lutadores(grafo)
print("Exemplo 1:")
print("É possível realizar a designação:", possivel)
if possivel:
    print("Designação:", designacao)

# Rodando um exemplo que não funciona:
# Representação do grafo como matriz de adjacência: 4 lutadores, com rivalidades entre (0,1), (0,2), (1,2) e (2,3)
grafo2 = [
    [0, 1, 1, 0],    #A
    [1, 0, 1, 0],    #B
    [1, 1, 0, 1],    #C
    [0, 0, 1, 0]     #D
]

possivel, designacao = classificar_lutadores(grafo2)
print("Exemplo 2:")
print("É possível realizar a designação:", possivel)
if possivel:
    print("Designação:", designacao)