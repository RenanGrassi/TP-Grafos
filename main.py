from grafo import Grafo

def main():
    #Arquivo grafo.txt já tem que estar criado!
    # grafo = Grafo("grafos/grafo2.txt")
    grafo = Grafo("grafos/grafo8.txt")
    
    # print("Ordem do Grafo:", grafo.ordem())
    # print("Tamanho do Grafo:", grafo.tamanho())
    # print("Densidade do Grafo:", grafo.densidade())
    # grafo.buscaEmLargura(2)
    # print(grafo.verifica_ciclo())
    # grafo.caminho_minimo_E_distancia(5) # O parâmentro será o vértice inicial


    #PARTE 2

    cobertura = grafo.cobertura_minima()
    # print("Cobertura mínima de vértices:", cobertura)
    print("emparelhamento máximo: ", grafo.emparelhamento_maximo())
    

if __name__ == "__main__":
    main()
   
    
