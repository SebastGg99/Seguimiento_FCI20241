# Clase fuerza de Lorentz

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

* "Seguimiento_1.py": contiene la definición de la clase partícula, que representa una partícula con propiedades como la masa, carga eléctrica, posición, velocidad y aceleración . Además de las interacciones entre ellas como se explicará en la siguiente sección.
* 'execution.py": es el archivo que instancia la clase, dando los parámetros mencionados anteriormente

# Uso

Para hacer uso del simulador, se debe importar la clase Particula en el execution desde el archivo "Seguimiento_1.py" y se deben crear las instanciar mediante las variables físicas que deseas controlar, tales como la masa, la carga, la posición inicial, la velocidad inicial y la aceleración. Todo eso para calcular el movimiento de las partículas y visualizar los resultados mediantes gráficas.

# Requisitos

* Python 3.x
* Numpy
* Matplotlib

# Descripción de las clases:

## Clase Particula:

Representa la creación del objeto con propiedades como carga y masa
Atributos:
    1.  carga (float): carga electrica de la partícula
    2.  masa (float): masa de la partícula

Metodos:
    1. __init__: constructos de la clase

## Clase Dinamica:
Calcula la evolución de la dinámica en función del tiempo, para las variables como posición, velocidad y aceleración.
Atributos:
    1.  posicion: posicion de la partícula
    2.  velocidad: velocidad inicial de la particula
    3.  aceleracion: aceleración inicial de la partícula
Métodos:
    1. __init__(): constructor de la clase, inicializa los atributos de la dinámica de la partícula. 
    2. TotalInteractio(): calcula la aceleración total de la partícula debido a la interacción mediante la fuerza de Lorentz.
    3. PasoTiempo(): realiza la integración numérica (evolución temporal de los atributos)

## Clase Plots:

Genera los gráficos de la trayectoria o de las coordenadas de las partículas en función del tiempo:
Atributos:
    -   sol1: solución de la dinámica de la partícula 1.
    -   sol2: solución de la dinámica de la partícula 2.

Metodos:
    -   __init__(): constructor para inicializar los atributos
    -   plot(): genera los gráficos de la trayectoria o de las coordenadas de acuerdo a la opcion suministrada.
# Contribiciones
Si encuentras algún bug en la implementación del código no dudes en notificarnos.

Desarrollado por Jose Luis Torres, Sebastián Gaviria, Mario José Félix.
# Referencias

[1] Jackson, John David, (1999). Classical electrodynamics. New York :Wiley
[2] Sepulveda, Alonso, (2009). Electromagnetismo. Universidad de Antioquia.
