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
        vertices = list(range(1, len(self.matriz_adjacencia) + 1))

        if v not in vertices:
            print("Vértice não pertence ao grafo")
            return

        #Define as estruturas que determinam o funcionamento do algoritmo
        Q = []
        marcado = []
        explorado = {}
        lista_explorado_nao_arvore = []
        pai = {}
        arvores = []

        if v in vertices and v not in marcado:
            #Inicia busca a partir do nó passado por parâmetro e inicializa fila Q
            arvore_atual = set()
            Q.append(v)
            marcado.append(v)
            arvore_atual.add(v)

            while len(Q) > 0:
                #Remove elemento de Q e trabalha sobre este
                vertice_atual = Q.pop(0)
                for w in self.vizinhos(vertice_atual):
                    #Nós pertencentes a árvore de busca
                    if w not in marcado:
                        explorado[(vertice_atual, w)] = True
                        Q.append(w)
                        marcado.append(w)
                        pai[w] = vertice_atual
                        arvore_atual.add(w)
                    else:
                        #Nós fora da árvore de busca principal
                        if pai.get(vertice_atual) != w:
                            aresta = (min(vertice_atual, w), max(vertice_atual, w))
                            if aresta not in lista_explorado_nao_arvore:
                                lista_explorado_nao_arvore.append(aresta)

            arvores.append(arvore_atual)
        #Algoritmo para busca em largura de grafos desconexos
        for vertice in sorted(vertices):
            if vertice not in marcado:
                arvore_atual = set()
                Q.append(vertice)
                marcado.append(vertice)
                arvore_atual.add(vertice)

                while len(Q) > 0:
                    vertice_atual = Q.pop(0)
                    for w in self.vizinhos(vertice_atual):
                        if w not in marcado:
                            explorado[(vertice_atual, w)] = True
                            Q.append(w)
                            marcado.append(w)
                            pai[w] = vertice_atual
                            arvore_atual.add(w)
                        else:
                            if pai.get(vertice_atual) != w:
                                aresta = (min(vertice_atual, w), max(vertice_atual, w))
                                if aresta not in lista_explorado_nao_arvore:
                                    lista_explorado_nao_arvore.append(aresta)

                arvores.append(arvore_atual)

        for i, arvore in enumerate(arvores, start=1):
            print(f"Árvore de busca em largura {i}: {sorted(arvore)}")
        print("Arestas não-árvore:", lista_explorado_nao_arvore)

    def verifica_ciclo(self):
        #Só pode ser ciclo se a ordem do grafo for superior a 2
        if self.ordem() > 2:
            matriz = self.matriz_adjacencia
            no = 0
            conta_aresta = 0
            candidato_ciclo = set()
            
            #Só é possível ser ciclo se o grau de cada vértice do ciclo for no mínimo 2
            #Mas, apenas isso não define um ciclo
            for vertice in matriz:
                no+=1
                if self.grau(no) >= 2:
                    for aresta in vertice:
                        if aresta != 0:
                            conta_aresta+=1
                        if conta_aresta >= 2:
                            candidato_ciclo.add(no)
                    conta_aresta = 0
           
            #Separa para análise os nós que podem estar em um ciclo
            nos_ciclo = [[] for _ in range(len(matriz[0]))]
            remove_nos = []
            for contador, k in enumerate(nos_ciclo):
                if contador + 1 not in candidato_ciclo:
                    remove_nos.append(contador)
            nos_ciclo = [sub for i, sub in enumerate(nos_ciclo) if i not in remove_nos]
            
            #Confere quantas vezes cada vértice aparece no grafo
            #Se os vértices não aparecem ao menos 2 vezes, não há ciclo
            for linha in matriz:
                for j in range(len(nos_ciclo)):
                    nos_ciclo[j].append(linha[j])
            difente0 = {i:0 for i in range(len(nos_ciclo))}
            for i in range(len(nos_ciclo)):
                if i+1 in candidato_ciclo:
                    difente0[i] = sum(1 for coluna in nos_ciclo if coluna[i] != 0) 

            for k in list(difente0.keys()):
                if difente0[k] == 0:
                    del difente0[k]
            
            todos_maiores_que_dois = all(valor >= 2 for valor in difente0.values())
            ciclo = "Há ciclo no grafo" if(todos_maiores_que_dois) else "Não há ciclos no grafo"
            print(ciclo)
            return todos_maiores_que_dois

        else:
            print("Não há ciclos no grafo")
            return False
    
    def componentesConexas(self):
        #Confere a quantidade de nós e prepara para criar busca em profundidade e armazenamento dos nós das componentes
        n = self.ordem()
        visitados = [False]*n
        componentesConexas = []
        
        #Se nó foi visitado, adiciona o nó a uma componente
        #Itera sobre todos os nós do grafo e realiza a busca em profundidade para adicionar os nós às suas respectivas componenentes
        #Ao final as componentes são adicionadas a uma lista que guarda todas as componentes produzidas
        def buscaEmProfundidadeAdaptada(v, no_componente):
            visitados[v] = True
            no_componente.append(v)
            for i in range(n):
                if self.matriz_adjacencia[v][i] != 0 and visitados[i] == False:
                    buscaEmProfundidadeAdaptada(i, no_componente)
        
        for v in range(n):
            if(not visitados[v]):
                no_componente = []
                buscaEmProfundidadeAdaptada(v, no_componente)
                componentesConexas.append(no_componente)

        qtdComponentes = len(componentesConexas)
        
        saidaQtdComponentes = f'{qtdComponentes} componente conexa' if qtdComponentes == 1 else f'{qtdComponentes} componentes conexas'
        print(saidaQtdComponentes)
        for i in range(len(componentesConexas)):
            print(componentesConexas[i])


