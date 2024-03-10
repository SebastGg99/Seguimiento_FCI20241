# Clase fuerza de Lorentz

Desarrollado por:

**Mario José Felix** \\
**José Luis Torres** \\
**Sebastián Gaviria**

En este proyecto buscamos simular el comportamiento de un sistema físico configurado por dos partículas puntuales cargadas, interaccionando con una intensidad de campo magnético y con el campo eléctrico generado por la otra partícula cargada. Como primera aproximación consideramos que los movimientos de las partículas son no relativistas, es decir, en el régimen donde la ley de Coulomb es aplicable y por lo tanto tenemos la siguiente expresión:

$$ \vec{F}_L = F_m+F_e \rightarrow \vec{F} = q\vec{v}\times \vec{B} + k\frac{q_1 q_2}{r^3}\vec{r}$$

Debido a las fuerzas mediadoras de la interacción, en la parte magnética de la fuerza de Lorentz, tenemos atributos propios de la partícula, tales como la carga, la masa, la velocidad, la posición inicial y además, se configura la aceleración para que esté inicializada a cero, estos son los atributos de cada partícula. Por otro lado, tenemos un parámetro, $\vec{B}$, puesto que la intensidad de campo magnético es una cantidad que se puede modificar de acuerdo al problema que se busca simular.

Para la mediadiadora entre las cargas eléctricas, tenemos que, la partícula a interacciona con la partícula b mediante la carga y la distancia que las separa, por lo tanto, necesitamos como parámetros, la posición de la partícula b y la carga,  así estos son los dos parámetros.

Puesto que cada fuerza mediadora genera una respectiva aceleración magnética y eléctrica, haciendo uso de la segunda ley de Newton $\vec{F} = \frac{d\vec{p}}{dt}$, teniendo en cuenta que la masa de las partículas en el límite no relativista no cambia con la velocidad, tenemos que dividir cada aceleración por la masa y sumarlas.

Como parte final del proyecto, haciendo uso de las ecuaciones cinemáticas del movimiento uniformemente acelerado (aceleración constante), tenemos las siguientes expresiones:

$$ \vec{r}(t) = \vec{r}_0+\vec{v}_0 t+\frac{1}{2}\vec{a}t^2 $$
Y
$$ \vec{v}(t) = \vec{v}_0+\vec{a}t $$

Por último, debemos analizar y extraer mediante gráficas, la trayectoria, velocidad y la aceleración de las partículas debido a las interacciones consideradas.


# Importancia de la fuerza de Lorentz

La fuerza de Lorentz es importante para estudiar los comportamientos generados por la interacción de partículas cargadas en movimiento en regiones de campos electricos e intensidades de campos magnéticos. Esto pues ayudó a establecer la relación carga-masa de los isótopos de los elementos, así como también la trayectoria que cumplen estas partículas, puesto que así, se pueden redireccionar en el campo de colisionadores o lásers.

# Contenido:

* **clase.py**: contiene la definición de la clase Particle, que representa una partícula con propiedades como la masa, carga eléctrica, posición, velocidad y aceleración . Además de las interacciones entre ellas como se explicará en la siguiente sección.
* **execution.py**: es el archivo que instancia la clase, dando los parámetros mencionados anteriormente.

# Uso

Para hacer uso del simulador, se debe importar la clase Particle en el ejecutable desde el archivo "clase.py" y se deben crear las instancias mediante las variables físicas que se desee controlar, tales como la masa, carga, posición inicial, velocidad inicial y aceleración. Todo eso para calcular el movimiento de las partículas y visualizar los resultados mediantes gráficas.

# Requisitos

* Python 3.x
* Numpy
* Matplotlib

# Descripción de la clase:

## Clase Particle:

Representa la creación del objeto con propiedades como carga, masa y sus variables dinámicas.

Atributos:

1. q1 (float): carga electrica de la partícula 1
2. m1 (float): masa de la partícula 1
3.  r1 (np.ndarray): posición inicial de la partícula 1
4.  v1 (np.ndarray): velocidad inicial de la partícula 1
5.  q2 (float): carga electrica de la partícula 2
6.  m2 (float): masa de la partícula 2
7.  r2 (np.ndarray): posición inicial de la partícula 2
8.  v2 (np.ndarray): velocidad inicial de la partícula 2
9.  t_end (float): tiempo de integración (default: 30)
10. num_steps (int): número de pasos en la integración (default: 300)

Metodos:

1.  __init__(): Constructos de la clase
2.  motion(): Realiza la simulación de la interacción entre las partículas y el campo magnético.
    A su vez, realiza la integración numérica que actualiza los estados de las partículas.
3.  plot_motion(): Genera los gráficos 3D de la trayectoria, o los gráficos 2D de las coordenadas, de acuerdo a la opcion suministrada.

# Contribiciones
Si encuentras algún bug en la implementación del código no dudes en notificarnos.

# Referencias

- Jackson, John David, (1999). Classical electrodynamics. New York :Wiley
- Sepulveda, Alonso, (2009). Electromagnetismo. Universidad de Antioquia.