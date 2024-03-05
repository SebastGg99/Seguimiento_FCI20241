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


# La clase Particula para usuarios:

Primero se crea el objeto partícula mediante la clase partícula, para llamarla por medio de una instancia debe proporcionar :
* Atributos: carga (float), masa (float), posición inicial (array), velocidad inicial (array)
Y a los métodos que puede acceder en la clase son:
* Métodos:
    1. Fuerza magnética: para llamar a este método necesita de tres parámetros, el tiempo(array) y la aceleración(array) que son los responsables de evolucionar la velocidad, y el campo magnético $\vec{B}$ (array) que media la interacción de la partícula con velocidad.
    2. Fuerza eléctrica: para llamar a este método necesita de la partícula 2(objeto), haciendo énfasis en la carga ($q_2$) y la posición de las partículas que se van modificando a medida que transcurre el tiempo. 
    3. Fuerza total: Ingresa los parámetros mencionados anteriormente y regresa la suma de las fuerzas de interacción 
    4. Aceleración total: Ingresa la fuerza total y retorna la aceleración total de la partícula. 
    5. Solución numérica, soluciona la evolución temporal de la partícula, es decir, obtiene la trayectoria, la velocidad y la aceleración.
    6. Grafica: grafica la trayectoria, velocidad y aceleración obtenida anteriormente.

# Referencias

[1] Jackson, John David, (1999). Classical electrodynamics. New York :Wiley
[2] Sepulveda, Alonso, (2009). Electromagnetismo. Universidad de Antioquia.
