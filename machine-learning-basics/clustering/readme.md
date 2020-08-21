agrupa objetos similares en clusters que los identifican.

se utiliza principalmente aprendizaje no supervisado que no requiere la utilización de etiquetas.

permite entender la estructura de los datos y la similitud entre los mismos.

básicamente nos permite detectar grupos en sets de datos complejos en los que no es evidente ninguna relación entre ellos.

Agrupamiento Jerárquico.
El algoritmo comienza tratando a cada objeto como un cluster individual y luego realiza los siguientes pasos de manera recursiva.

1.  identifica a los dos clusters con menor distancia (los mas similares)
2.  agrupa a los dos cluster en uno nuevo.

el output final es un dendrograma que muestra la relación entre objetos y grupos.

es importante determinar qué medida y método vamos a utilizar para el cálculo de distancia (Euclidiana, Manhattan, etc.) y los puntos de referencia para el cálculo a utilizar en cada cluster (linkage criteria).
