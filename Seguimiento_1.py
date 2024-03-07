import numpy as np
import matplotlib.pyplot as plt

class Particula:
  """ Clase Particula 
  Esta clase representa una partícula cuyos atributos son la carga y la masa
  Atributos:
    - carga (float): carga eléctrica de la partícula
    - masa (float): masa de la partícula

  Métodos:
    - Constructor de la clase encargado de inicializar los atributos de la partícula
  """
  def __init__(self, q, m):
    """Inicializamos los atributos del objeto"""
    self.carga = q
    self.masa = m

class Dinamica:
  """Clase dinámica
  Esta clase se encarga de hacer la dinámica y cinemática de la partícula, incluye la posición, velocidad y aceleración en función del tiempo
  Atributos:
    - posición (r0-array): posición inicial de la partícula
    - velocidad (v0-array): velocidad inicial de la partícula
    - aceleracion (a0-array): aceleración inicial de la partícula.

  Métodos:
    - __init__(): constructor de la clase, se encarga de inicializar los atributos de la partícula
    - TotalInteraction(): Calcula la aceleración total de la partícula debido a la interacción mediante la fuerza de Lorentz
    - PasoTiempo(): realiza integración numérica para calcular las variables de estado (posición, velocidad y aceleración) de la partícula.

  """
  def __init__(self, r0, v0, a0 = np.zeros(3)):
    self.posicion = r0
    self.velocidad = v0
    self.aceleracion = a0

  def TotalInteraction(self, posicion1, posicion2, velocidad, carga1, carga2, masa, campoB, k = 9e+9):
    """ Método TotalInteraction
    Inputs:
      - posicion1 (array): posición de la partícula con la que interactúa
      - posicion2 (array): posición de la propia partícula
      - velocidad (array): velocidad de la partícula
      - carga1 (float): carga eléctrica de la partícula con la que interactúa
      - carga2 (float): carga eléctrica de la propia partícula
      - masa (float): masa de la partícula
      - campoB (array): campo magnético externo.
      - k: Constante de Coulomb por defecto es 9e+9
    
    Outputs:
      - a_T (array): aceleración total de la partícula
    """
    F_L = carga1 * np.cross(velocidad, campoB)
    a_L = F_L / masa

    C = k * carga1 * carga2
    dir = posicion2 - posicion1
    r = np.linalg.norm(dir)
    F_C = (C * dir) / (r**3)
    a_C = F_C / masa

    a_T = a_L + a_C
    return a_T

  def PasoTiempo(self, posicion1, posicion2, velocidad, carga1, carga2, masa, campoB, t, dt):
    """Método PasoTiempo
    Este método realiza la integración numérica para calcular la posición, velocidad y aceleración de la partícula en función del tiempo
    Inputs:
      - posicion1 (array): posicon de la partícula 1
      - posicion2 (array): posicion de la partícula 2
      - velocidad (array): velocidad de la partícula
      - carga1 (float): carga elecrtica de la partícula 1
      - carga2 (float): carga electrica de la partícula 2
      - campoB (float): campo magnético externo 
      - t (int o float): tiempo total de la simulación
      - dt (float): paso de tiempo para realizar la integración

    Outputs:
      - Posicion (array): posicion de la partícula evolucionada temporalmente
      - Velocidad (array): velocidad de la partícula evolucionada temporalmente
      - Aceleracion(array): aceleracion de la partícula evolucionada temporalmente.
    """
    t_ = np.arange(0, t + dt, dt)
    Posicion = np.zeros((len(t_), 3))
    Posicion[0] = self.posicion
    Velocidad = np.zeros_like(Posicion)
    Velocidad[0] = self.velocidad
    Aceleracion = np.zeros_like(Posicion)
    Aceleracion[0] = self.aceleracion

    for j in range(len(t_) - 1):
      Aceleracion[j + 1] = self.TotalInteraction(Posicion[j], posicion2, Velocidad[j], carga1, carga2, masa, campoB)
      Velocidad[j + 1] = Velocidad[j] + Aceleracion[j] * dt
      Posicion[j + 1] = Posicion[j] + Velocidad[j] * dt + 0.5 * Aceleracion[j] * (dt**2)

    return Posicion, Velocidad, Aceleracion

class Plots:
  """Clase Plots
  Clase encargada de generar los gráficos de la trayectoria o coordenadas de las partículas en función del tiempo
  Atributos:
    - sol1: solución de la dinámica de la partícula 1
    - sol2: solución de la dinámica de la partícula 2
  Métodos:
    -__init__(): Inicializa los atributos de la clase.
    -plot(): genera un gráfico de la trayectoria o de las coordenadas de las partículas en función del tiempo, como función de la opción ingresada.
  """

  def __init__(self, sol1, sol2):
    self.sol1 = sol1
    self.sol2 = sol2

  def plot(self, t, dt, option = "Trayectoria"):
    """Método plot
    Genera gráfico de la trayectoria o de las coordenadas de las partículas en función del tiempo
    Inputs:
      - t (int o float): tiempo total de la simulación
      - dt (float): paso de tiempo para la integración
      - option (str): opción para seleccionar qué tipo de gráfico generar ("Trayectoria" o "x(t)")
    """
    t_ = np.arange(0, t + dt, dt)
    x1 = [i[0] for i in self.sol1[0]]
    y1 = [i[1] for i in self.sol1[0]]
    z1 = [i[2] for i in self.sol1[0]]

    x2 = [i[0] for i in self.sol2[0]]
    y2 = [i[1] for i in self.sol2[0]]
    z2 = [i[2] for i in self.sol2[0]]
    if option == "Trayectoria":
      fig = plt.figure()
      ax = fig.add_subplot(111, projection='3d')
      ax.plot(x1, y1, z1)
      ax.plot(x2, y2, z2)

      ax.quiver(x1[:-1], y1[:-1], z1[:-1], np.diff(x1), np.diff(y1), np.diff(z1), color='b', length=0.2, normalize=True)
      ax.quiver(x2[:-1], y2[:-1], z2[:-1], np.diff(x2), np.diff(y2), np.diff(z2), color='r', length=0.2, normalize=True)

      # Etiquetas de los ejes
      ax.set_xlabel('X')
      ax.set_ylabel('Y')
      ax.set_zlabel('Z')

      # Mostrar la gráfica
      plt.show()
    
    elif option == "x(t)":
      fig, ax = plt.subplots(2, 3, figsize=(15, 10))
      ax[0,0].plot(t_, x1, 'r')
      ax[0,0].set_title('x_1(t)')
      ax[0,1].plot(t_, y1, 'r')
      ax[0,1].set_title('y_1(t)')
      ax[0,2].plot(t_, z1, 'r')
      ax[0,2].set_title('z_1(t)')
      ax[1,0].plot(t_, x2, 'b')
      ax[1,0].set_title('x_2(t)')
      ax[1,1].plot(t_, y2, 'b')
      ax[1,1].set_title('y_2(t)')
      ax[1,2].plot(t_, z2, 'b')
      ax[1,2].set_title('z_2(t)')

      plt.tight_layout()

      plt.show()

q1 = 1
q2 = -1
m1 = 1
m2 = 1
r1 = np.array([10, 20, 30])
v1 = np.array([1, 2, 5])
r2 = np.array([-11, 2, -40])
v2 = np.array([2, 3, 4])
campoB = np.array([5, 0, 0])
t = 10
dt = t / 1000

p1 = Particula(q1, m1)
p2 = Particula(q2, m2)

d1 = Dinamica(r1, v1)
d2 = Dinamica(r2, v2)

a1 = d1.TotalInteraction(r1, r2, v1, q1, q2, m1, campoB)
a2 = d1.TotalInteraction(r2, r1, v2, q1, q2, m2, campoB)

sol1 = d1.PasoTiempo(r1, r2, v1, q1, q2, m1, campoB, t, dt)
sol2 = d2.PasoTiempo(r2, r1, v2, q1, q2, m2, campoB, t, dt)

plot = Plots(sol1, sol2)

plot.plot(t, dt)