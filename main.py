from grafo import Grafo

def main():
    grafo = Grafo("grafos/grafo2.txt")
    
    print("\nOrdem do Grafo:", grafo.ordem())

    print("\nTamanho do Grafo:", grafo.tamanho())

    print(f"\nDensidade do Grafo: {grafo.densidade():.2f}")

    print("\nVizinhos do vértice 5:", grafo.vizinhos(5))

    print("\nGrau do vértice 5:", grafo.grau(5))

    print("\nVértice 5 do grafo é articulação:", grafo.e_articulacao(5))

    grafo.buscaEmLargura(2)
    
    grafo.componentesConexas()
    
    tem_ciclo = grafo.verifica_ciclo()

    print(f"\n{grafo.caminho_minimo_E_distancia(3)}\n") # O parâmetro será o vértice inicial
    

if __name__ == "__main__":
    main()
