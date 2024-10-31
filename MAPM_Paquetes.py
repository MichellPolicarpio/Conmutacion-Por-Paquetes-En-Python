# Policarpio Moran Michell Alexis - zS21002379 - IINF - FIEE - UV
# Programación de Redes
# Simulación de conmutación por paquetes con grafos en Python

import networkx as nx
import matplotlib.pyplot as plt
import time
import random

# se crea un grafo
G = nx.Graph()

# se agregan nodos manualmente
G.add_node("A", mensaje="Ella rompió sus cadenas y convirtió el fuego en lluvia")  # Nodo A almacena el mensaje
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node("B") #Este nodo recibira el mensaje almacenando dicha cadena 

# agrego  aristas con etiquetas 
G.add_edge(1, "A", label="a")
G.add_edge(1, 2, label="e")
G.add_edge(1, 3, label="c")
G.add_edge(1, 4, label="d")
G.add_edge(5, 2, label="h")
G.add_edge(3, 6, label="f")
G.add_edge(4, 5, label="i")
G.add_edge(4, 3, label="g")
G.add_edge(6, 5, label="j")
G.add_edge("B", 6, label="l")

# (NOTITA) Los nodos agregados y sus respectivas conexiones me basé en en un grafo del ejemplo de las diapositivas

# Función para mostrar el grafo con etiquetas
def imprimirGrafo(G):
    pos = nx.spring_layout(G)  # funcion para que genere utomáticamente posiciones de los nodos
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black')  # se dinujan los nodos y aristas
    edge_labels = nx.get_edge_attributes(G, 'label')  # se obtiene etiquetas de las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)  # aqui dibujo etiquetas de aristas
    plt.title('Grafo con Etiquetas de Aristas')
    plt.show()

# Función para dividir el mensaje en "paquetes" (aqui partimos la cadena para simular enviarlos como cadena)
def dividirMensaje(mensaje, tamañoADividir):
    paquetes = []
    i = 0
    while i < len(mensaje):
        paquete = mensaje[i:i+tamañoADividir]
        paquetes.append(paquete)
        i += tamañoADividir
    return paquetes

# Función para simular (o asignar) el envío de paquetes por múltiples caminos hasta el nodo destino
def simulacionEnvioPorPaquetes(G, nodoInicial, nodoFinal):
    if "mensaje" not in G.nodes[nodoInicial]:
        print(f"El nodo {nodoInicial} no tiene un mensaje para enviar.")
        return

    # obtener el mensaje del nodo inicial
    mensaje = G.nodes[nodoInicial]["mensaje"]
    paquetes = dividirMensaje(mensaje, tamañoADividir=15)
    
    # inicializar el almacenamiento del mensaje en el nodo final
    G.nodes[nodoFinal]["mensaje"] = ""
    
    #obtener todos los caminos posibles
    caminos = list(nx.all_simple_paths(G, source=nodoInicial, target=nodoFinal))
    
    for paquete in paquetes:
        print(f"\nPaquete '{paquete}'")
        time.sleep(1)
        
        # Seleccionar un camino aleatorio para cada paquete
        camino = random.choice(caminos)
        print(f"  Camino: {camino}")
        for i in range(len(camino) - 1):
            nodoActual = camino[i]
            nodoSig = camino[i + 1]
            etiq_Arista = G[nodoActual][nodoSig]['label']  # Almacena la etiqueta de la arista entre dos nodos determinados
            print(f"    Enviando mensaje fragmentado de NODO A través de arista {etiq_Arista}")
            time.sleep(0.2)
        
        # aqui se almacena el paquete en el nodo final
        G.nodes[nodoFinal]["mensaje"] += paquete
    
    print("\nMensaje completo reensamblado en el destino NODO B:", G.nodes[nodoFinal]["mensaje"])

# Llamada a la función para el envío del mensaje desde el nodo A al nodo B
simulacionEnvioPorPaquetes(G, "A", "B")

time.sleep(2)

# se imprime el grafo respectivo 
imprimirGrafo(G)