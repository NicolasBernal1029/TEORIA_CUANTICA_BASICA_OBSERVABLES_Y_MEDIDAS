## BASIC-QUANTUM-THEORY
Este repositorio contiene los códigos utilizados en el capítulo 4 del libro "Quantum Computing for Computer Scientists" de Noson S. Yanofsky y Mirco A. Mannucci. El capítulo trata sobre los conceptos básicos de la teoría cuántica, incluyendo la notación de Dirac, los estados cuánticos y las mediciones, y cómo estos conceptos se aplican en la construcción de algoritmos cuánticos.

## Contenido
BasicQuantumTheory.py: este archivo contiene la clase Particle que se utiliza para representar partículas cuánticas. Incluye métodos para calcular la probabilidad de encontrar una partícula en una posición determinada, la probabilidad de transición entre dos partículas y la amplitud de transición entre dos partículas. También se incluyen métodos para calcular la media y la varianza de un observable y las probabilidades asociadas a los valores propios de un observable. Por último, se incluye un método para evolucionar un estado cuántico dado una lista de matrices de evolución.

test.py: este archivo contiene los casos de prueba para la clase Particle.

## Notas Importantes
Asegúrate de que los estados cuánticos de entrada estén adecuadamente normalizados (la suma de los cuadrados absolutos debe ser igual a 1).
Al utilizar mean_and_variance y eigenvalues_and_probabilities, asegúrate de proporcionar operadores observables hermíticos.
Siéntete libre de modificar y expandir la clase para adaptarla a tus necesidades específicas de simulación cuántica.

Define tu partícula cuántica creando una instancia de la clase Particle. Debes proporcionar los siguientes parámetros:

n: Dimensión del estado cuántico.
ket: El vector de estado cuántico (ket) con el que deseas trabajar.
ket_evolve: El ket inicial para la evolución.

Utiliza los métodos disponibles para analizar y simular el comportamiento cuántico:

probability(posición): Calcula la probabilidad de encontrar la partícula en una posición específica.
transition_probability(otra): Calcula la probabilidad de transición entre dos estados cuánticos.
transition_amplitude(otra): Calcula la amplitud de transición entre dos estados cuánticos.
mean_and_variance(observable): Calcula la media y la varianza de un operador observable.
eigenvalues_and_probabilities(observable): Calcula los eigenvalores, eigenvectores y sus probabilidades correspondientes para un operador observable.
evolve(lista_U): Realiza la evolución cuántica de la partícula utilizando una lista de operadores unitarios.

## Requisitos
Python 3.x
numpy
## Ejecución de pruebas
Para ejecutar las pruebas, ejecute el siguiente comando en la línea de comandos: python -m unittest test.py

## Referencias
Yanofsky, N. S., & Mannucci, M. A. (2013). Quantum computing for computer scientists. Cambridge University Press.

