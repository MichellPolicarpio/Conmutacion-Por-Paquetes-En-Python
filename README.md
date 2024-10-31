# 🌐 Simulación de Conmutación por Paquetes con Grafos

Este proyecto implementa una simulación de conmutación por paquetes utilizando grafos en Python, desarrollado como parte del curso de Programación de Redes en la Facultad de Ingeniería Eléctrica y Electrónica (FIEE) de la Universidad Veracruzana (UV).

## 👨‍💻 Autor
- **Nombre:** Policarpio Moran Michell Alexis
- **Matrícula:** zS21002379
- **Programa:** Ingeniería Informática
- **Facultad:** FIEE - UV

## 📝 Descripción
El programa simula el proceso de conmutación por paquetes en una red utilizando grafos. Implementa la fragmentación de mensajes en paquetes más pequeños y su transmisión a través de diferentes rutas en la red, similar a cómo funciona el enrutamiento de paquetes en redes reales.

## ⭐ Características
- 📊 Creación y visualización de grafos utilizando NetworkX
- 📦 Fragmentación de mensajes en paquetes más pequeños
- 🔄 Simulación de envío de paquetes por múltiples rutas
- 🎯 Visualización de la topología de red con etiquetas en las aristas
- 🔄 Reensamblaje de mensajes en el nodo destino

## 🛠️ Requisitos
```python
networkx
matplotlib
```

## 🗺️ Estructura del Grafo
- El grafo contiene 8 nodos (A, B, 1-6)
- El nodo A contiene el mensaje inicial
- El nodo B es el destino final
- Las aristas están etiquetadas de 'a' a 'l'
- La topología está basada en ejemplos de redes de conmutación por paquetes

## 🔧 Funcionalidades Principales
1. `imprimirGrafo(G)`: Visualiza el grafo con sus nodos y aristas etiquetadas
2. `dividirMensaje(mensaje, tamañoADividir)`: Fragmenta el mensaje en paquetes más pequeños
3. `simulacionEnvioPorPaquetes(G, nodoInicial, nodoFinal)`: Simula el envío de paquetes por diferentes rutas

## 💡 Ejemplo de Uso
El programa incluye una demostración que:
1. 📤 Envía el mensaje "Ella rompió sus cadenas y convirtió el fuego en lluvia"
2. ✂️ Divide el mensaje en paquetes de 15 caracteres
3. 🔄 Envía cada paquete por una ruta aleatoria
4. 📥 Reensambla el mensaje en el nodo destino

## 🎨 Visualización
El programa genera una visualización del grafo utilizando matplotlib, donde:
- 🔵 Los nodos se muestran en color azul claro
- ⚫ Las aristas se muestran en negro
- 🏷️ Las etiquetas de las aristas son visibles
- 🎯 La disposición de los nodos se genera automáticamente usando el algoritmo spring_layout

## 📌 Notas
- ⏰ Los retardos (time.sleep) se incluyen para simular el tiempo de transmisión
- 🎲 La selección de rutas es aleatoria para cada paquete
- ✅ El programa verifica la existencia del mensaje en el nodo inicial antes de comenzar la transmisión
