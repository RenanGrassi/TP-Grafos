# grafo.py

class Grafo:
    def __init__(self, caminho_arquivo):
        "Inicializa e lê arquivo .txt"
        self.matriz_adjacencia = []
        self.carregar_grafo(caminho_arquivo)
    
    def carregar_grafo(self, caminho_arquivo):
        "Lê o grafo do txt e armazena na matriz de adjacência"
        with open(caminho_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            num_vertices = int(linhas[0].strip())
            self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]
            
            for linha in linhas[1:]:
                u, v, peso = linha.split()
                #Ajusta índice zero
                u, v = int(u) - 1, int(v) - 1  
                peso = float(peso)
                self.matriz_adjacencia[u][v] = peso
                #Grafo não direcionado
                self.matriz_adjacencia[v][u] = peso
    
    def ordem_do_grafo(self):
        "Número de vértices do grafo"
        return len(self.matriz_adjacencia)

    def tamanho_do_grafo(self):
        "Número de arestas do grafo"
        arestas = sum(1 for i in range(self.ordem_do_grafo()) for j in range(i) if self.matriz_adjacencia[i][j] != 0)
        return arestas
