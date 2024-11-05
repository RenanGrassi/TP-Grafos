from grafo import Grafo

def main():
    #Arquivo grafo.txt já tem que estar criado!
    grafo = Grafo("grafo.txt") 
    
    print("Ordem do Grafo:", grafo.ordem_do_grafo())
    print("Tamanho do Grafo:", grafo.tamanho_do_grafo())

if __name__ == "__main__":
    main()