from grafo import Grafo

def main():
    grafo = Grafo("grafos/grafo2.txt")
    
    cobertura = grafo.cobertura_minima()
    print("Cobertura mínima de vértices:", cobertura)

if __name__ == "__main__":
    main()
