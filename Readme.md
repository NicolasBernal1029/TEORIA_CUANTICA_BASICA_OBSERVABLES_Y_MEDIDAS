## BASIC-QUANTUM-THEORY
Este repositorio contiene los códigos utilizados en el capítulo 4 del libro "Quantum Computing for Computer Scientists" de Noson S. Yanofsky y Mirco A. Mannucci. El capítulo trata sobre los conceptos básicos de la teoría cuántica, incluyendo la notación de Dirac, los estados cuánticos y las mediciones, y cómo estos conceptos se aplican en la construcción de algoritmos cuánticos.

## Contenido
BasicQuantumTheory.py: este archivo contiene la clase Particle que se utiliza para representar partículas cuánticas. Incluye métodos para calcular la probabilidad de encontrar una partícula en una posición determinada, la probabilidad de transición entre dos partículas y la amplitud de transición entre dos partículas. También se incluyen métodos para calcular la media y la varianza de un observable y las probabilidades asociadas a los valores propios de un observable. Por último, se incluye un método para evolucionar un estado cuántico dado una lista de matrices de evolución.

test.py: este archivo contiene los casos de prueba para la clase Particle.

## Requisitos
Python 3.x
numpy
## Ejecución de pruebas
Para ejecutar las pruebas, ejecute el siguiente comando en la línea de comandos: python -m unittest test.py

## Referencias
Yanofsky, N. S., & Mannucci, M. A. (2013). Quantum computing for computer scientists. Cambridge University Press.

