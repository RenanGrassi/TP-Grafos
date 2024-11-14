from grafo import Grafo

def main():
    #Arquivo grafo.txt já tem que estar criado!
    ##grafo = Grafo("grafo2.txt")
    grafo = Grafo("grafo2.txt")
    
    print("Ordem do Grafo:", grafo.ordem())
    print("Tamanho do Grafo:", grafo.tamanho())
    print("Densidade do Grafo:", grafo.densidade())
    grafo.buscaEmLargura(2)
    print(grafo.verifica_ciclo())

if __name__ == "__main__":
    main()
