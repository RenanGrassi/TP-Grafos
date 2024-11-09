# grafo.py

class Grafo:
    def __init__(self, caminho_arquivo):
        "Inicializa e lê arquivo .txt"
        self.matriz_adjacencia = []
        self.carregar_grafo(caminho_arquivo)
    
    def carregar_grafo(self, caminho_arquivo):
   # "Lê o grafo do txt e armazena na matriz de adjacência"
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
    
    def ordem(self):
        "Número de vértices do grafo"
        return len(self.matriz_adjacencia)

    def tamanho(self):
        "Número de arestas do grafo"
        arestas = sum(1 for i in range(self.ordem()) for j in range(i) if self.matriz_adjacencia[i][j] != 0)
        return arestas
    
    def densidade(self):
        "Retorna a densidade do grafo"
        V = self.ordem()
        A = self.tamanho()
        if V > 1:
            return (2 * A) / (V * (V - 1))
        else:
            return 0  
    
    def vizinhos(self, vertice):
       # "Retorna uma lista dos vizinhos de um vértice fornecido"
        V = self.ordem()  
        vertice -= 1  # Ajusta para índice zero
    
        if vertice < 0 or vertice >= V:
            raise ValueError("Vertice fora dos limites")

        vizinhos = [i + 1 for i in range(V) if self.matriz_adjacencia[vertice][i] != 0]
        return vizinhos

    def grau(self, vertice):
      #  "Retorna o grau de um vértice fornecido"
        
        V = self.ordem()  
        vertice -= 1  # Ajusta para índice zero
        if vertice < 0 or vertice >= V:
            raise ValueError("Vertice fora dos limites")

        grau = sum(1 for i in range(V) if self.matriz_adjacencia[vertice][i] != 0)
        return grau
    
    # Função busca em profundidade
    def dfs(self, v, visitado, ignorar):
      #  "Função auxiliar DFS(busca em profundidade) que ignora o vértice especificado"
        visitado[v] = True
        for i in range(self.ordem()):
            if i != ignorar and self.matriz_adjacencia[v][i] != 0 and not visitado[i]:
                self.dfs(i, visitado, ignorar)

    def e_articulacao(self, vertice):
       # "Verifica se o vértice fornecido é uma articulação"
    
        vertice -= 1  # Ajusta para índice zero
        V = self.ordem()

        # Realiza uma DFS sem o vértice para verificar conectividade
        visitado = [False] * V
        start = 0 if vertice != 0 else 1  # Ponto inicial diferente do vértice a ser removido
        self.dfs(start, visitado, vertice)

        # Se há vértices não visitados, o grafo se desconecta ao remover 'vertice'
        return not all(visitado[i] or i == vertice for i in range(V))
    
    def buscaEmLargura(self, v):
        Q = []
        marcado = []
        explorado = {}
        lista_explorado_nao_arvore = []
        pai = {}
        nos = set()
        nos.add(v)
        marcado.append(v)
        Q.append(v)
        while(len(Q) > 0):
            v =  Q.pop(0)
            for w in self.vizinhos(v):
                if(w not in marcado):
                    explorado[(v,w)] = True
                    Q.append(w)
                    marcado.append(w)
                    pai[w] = v
                    nos.add(w)
                else:
                    if pai[v] != w:
                        aresta = (min(v,w), max(v,w))
                        if aresta not in lista_explorado_nao_arvore:
                            lista_explorado_nao_arvore.append((v,w))
        print(nos)
        print(lista_explorado_nao_arvore)
