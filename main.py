from grafo import Grafo

def main():
    #Arquivo grafo.txt já tem que estar criado!
    grafo = Grafo("grafo.txt") 
    
    print("Ordem do Grafo:", grafo.ordem())
    print("Tamanho do Grafo:", grafo.tamanho())
    print("Densidade do Grafo:", grafo.densidade())

if __name__ == "__main__":
    main()