# Resolución de Cubos Rubik

### Código del Proyecto: `rubik-cube`

### Estudiante: Rocío Corral

<img src="https://user-images.githubusercontent.com/69587750/139362634-e8ff2b1f-3eed-465d-921e-73705015923b.png" alt="Rubik Cube" width="200"/>

## Descripción

El cubo rubik o cubo mágico es un puzzle combinatorio tridimensional consistente en un cubo donde cada una de las seis caras tiene un color distinto y a su vez dicha cara está dividida en 9 cuadrados (distribuídos en una cuadrícula de 3x3). En este puzzle se puede rotar cada cara sobre su propio eje y el desafío es, únicamente mediante la rotación de las distintas caras, mezlar los colores del cubo y luego lograr volver al estado original en donde cada cara tiene cuadrados de un único color.

Este cubo tiene más de 43 trillones de posibles estados o permutaciones distintas de sus piezas y sólo se considera a uno de todos esos estados como la solución. Como ya se dijo, ese único estado es aquel en el que cada cara tiene un solo color. Mediante distintas demostraciones y desarrollos matemáticos, se ha logrado probar que 20 movimientos es el número mínimo en que se puede resolver cualquiera de las 43 trillones de pemutaciones posibles del cubo.

Dado este problema o puzzle a resolver, se busca implementar un algoritmo de Inteligencia Artificial que aprenda a resolver un cubo rubik de 3x3 sin ningún conocimiento a priori más que el estado objetivo del cubo (tener cada cara completa de un solo color) y los 12 movimientos posibles que se pueden hacer sobre las caras del cubo. 

En la práctica, el algoritmo debería ser capaz de llegar al estado objetivo a partir de cualquier estado del cubo alcanzado a través de la ejecución de n cantidad de movimientos de las caras del cubo partiendo del estado objetivo o armado. Esto se debe a la matemática intrínseca del cubo, ya que si se elige la distribución de colores o piezas del cubo de forma completamente aleatoria, es posible que el problema quede en un estado irresolubre mediante sólo los 12 movimientos posibles del cubo. 

El desempeño del algoritmo se medirá en primera instancia, considerando si el algoritmo alcanzó el estado objetivo. En caso de no alcanzarlo tras una determinada cantidad de iteraciones, se considerará qué tan cerca está el cubo del estado objetivo, es decir, de estar armado (medido en cantidad de piezas por cara correctamente colocadas). En caso de alcanzar la solución, se medirá en cuántas iteraciones lo logró y/o en cuantos movimientos lo logró (teniendo en consideración que el ideal son 20 movimientos), a su vez que se medirá cuánto tiempo tomó en ejecutar el algoritmo.

Estas métricas se tomarán sobre una cantidad predeterminada (mayor que uno) de ejecuciones del algoritmo. Partiendo, en primera instancia, de estados siempre iguales; y en segunda instancia, de estados distintos generados a través de m movimientos aleatorios. Esta decisión en las mediciones radica en que el algoritmo no es determinístico, de modo que se buscará obtener métricas confiables evaluando la media y la desviación estándar de los resultados de cada ejecución, para a su vez poder cuantificar hasta qué punto influye la aleatoriedad en estos resultados.

### Bibliografía

AIMA 3rd Edition - Chapters 4.1 (Genetic Algorithms) and 21 (Reinforcement Learning)

[Novel Rubik’s Cube Problem Solver by Combining Group Theory and Genetic Algorithm](https://link.springer.com/article/10.1007/s42979-019-0054-4)

[Solving the Rubik’s cube with deep reinforcement learning and search](https://openreview.net/pdf?id=Hyfn2jCcKm)

[The Mathematics of the Rubik’s Cube](https://web.mit.edu/sp.268/www/rubik.pdf)

## Justificación

Un cubo rubik clásico, de dimensión 3x3, tiene más de 43 trillones de posibles estados distintos a los que se puede llegar partiendo desde el estado armado simplemente rotando sus caras. Teniendo en cuenta esta gran cantidad de estados y considerando a su vez que el estado objetivo (o estado armado) es únicamente uno, se revela a simple vista que una aproximación para resolver este problema mediante fuerza bruta es inviable.

Cuando una persona se enfrenta a este puzzle, la solución se alcanza paso a paso observando el estado actual del cubo, ejecutando una secuencia específica de movimientos para llegar a otro estado más cercano a la solución y repitiendo con secuencias de movimientos cada vez más complejas (para no revertir el trabajo ya hecho en los pasos previos). Desde esta perspectiva, se podría programar un algoritmo de estados finitos, que determine el estado del cubo y en base a esto decida qué secuencia de movimientos de las provistas ejecuta. Si bien este enfoque es más factible, aún requiere que clasifiquemos todos los estados posibles del cubo en "grupos" de estados compatibles con cada secuencia de movimientos. Una solución de este tipo, si bien factible, implicaría obligar a la computadora a resolver el cubo como un humano lo haría, lo cual es una limitación al poder de cómputo del que disponemos. 

La idea detrás de usar un algoritmo de Inteligencia Artificial como lo es Reinforcement Learning o un algoritmo genético, es lograr no sólo que la computadora resuelva el cubo, sino que _aprenda_ a hacerlo a partir de un conjunto de reglas pequeño y simple. De modo que podamos observar cómo aprende a hacerlo y a su vez qué tan eficientemente lo hace, siendo esto es algo que no se puede lograr a través de los enfoques previos, en donde se provee al algoritmo con la totalidad de las reglas y únicamente debe aplicarlas en orden, de forma determinística.

## Listado de actividades a realizar

**Actividad 1:** investigación de bibliografía y planteos previos del mismo problema. _[3 días]_

**Actividad 2:** maquetado/diagramado del algoritmo y arquitectura del proyecto. _[2 días]_

**Actividad 3:** creación de la estructura `Cubo` y las 12 acciones (funciones) que lo modifican. _[1 día]_

**Actividad 4:** implementación del algoritmo genético. _[7 días]_ 

**Actividad 5:** ajuste de parámetros para optimizar el rendimiento. _[1 día]_

**Actividad 6:** análisis de resultados y obtención de métricas. _[1 día]_

**Actividad 7:** análisis de métricas y desarrollo de la conclusión. _[1 día]_

**Actividad 8:** elaboración del informe final. _[5 días]_

#### Actividades tentativas:

**Actividad 1.1:** investigar sobre Reinforcement Learning. _[2 días]_

**Actividad 4.1:** segunda implementación de la solución mediante Reinforcement Learning. _[10 días]_ 

**Actividad 6.1:** comparación del desempeño de ambos algoritmos. _[1 día]_

## Cronograma estimado de actividades

![imagen](https://user-images.githubusercontent.com/69587750/140009878-17bf58ea-38d0-4f79-8efa-6ea055aaa9a5.png)
