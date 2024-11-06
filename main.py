from grafo import Grafo

def main():
    #Arquivo grafo.txt já tem que estar criado!
    grafo = Grafo("grafo.txt") 
    
    print("Ordem do Grafo:", grafo.ordem())
    print("Tamanho do Grafo:", grafo.tamanho())
    print("Densidade do Grafo:", grafo.densidade())
    print("Vizinhos do vértice 2:", grafo.vizinhos(2))
    print("Grau do vértice 5:", grafo.grau(5))
    print("O vértice 2 é uma articulação: ", grafo.e_articulacao(2))
    print("O vértice 5 é uma articulação: ", grafo.e_articulacao(5))

if __name__ == "__main__":
    main()