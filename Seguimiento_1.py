import numpy as np
import matplotlib.pyplot as plt

class Particula:
  def __init__(self, q, m):
    self.carga = q
    self.masa = m

class Dinamica:
  def __init__(self, r0, v0, a0 = np.zeros(3)):
    self.posicion = r0
    self.velocidad = v0
    self.aceleracion = a0

  def TotalInteraction(self, posicion1, posicion2, velocidad, carga1, carga2, masa, campoB, k = 9e+9):
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
  def __init__(self, sol1, sol2):
    self.sol1 = sol1
    self.sol2 = sol2

  def plot(self, t, dt, option = "Trayectoria"):
    t_ = np.arange(0, t + dt, dt)
    
    x1 = [i[0] for i in self.sol1[0]]
    y1 = [i[1] for i in self.sol1[0]]
    z1 = [i[2] for i in self.sol1[0]]

    x2 = [i[0] for i in self.sol2[0]]
    y2 = [i[1] for i in self.sol2[0]]
    z2 = [i[2] for i in self.sol2[0]]

    vx1 = [i[0] for i in self.sol1[1]]
    vy1 = [i[1] for i in self.sol1[1]]
    vz1 = [i[2] for i in self.sol1[1]]
    
    vx2 = [i[0] for i in self.sol2[1]]
    vy2 = [i[1] for i in self.sol2[1]]
    vz2 = [i[2] for i in self.sol2[1]]

    ax1 = [i[0] for i in self.sol1[2]]
    ay1 = [i[1] for i in self.sol1[2]]
    az1 = [i[2] for i in self.sol1[2]]
    
    ax2 = [i[0] for i in self.sol2[2]]
    ay2 = [i[1] for i in self.sol2[2]]
    az2 = [i[2] for i in self.sol2[2]]
    
    if option == "Trayectoria":
      fig = plt.figure()
      ax = fig.add_subplot(111, projection='3d')
      ax.plot(x1, y1, z1)
      ax.plot(x2, y2, z2)

      # Etiquetas de los ejes
      ax.set_xlabel('X')
      ax.set_ylabel('Y')
      ax.set_zlabel('Z')

      # Mostrar la gráfica
      plt.show()
    
    elif option == "r(t)":
      fig, ax = plt.subplots(2, 3, figsize=(15, 10))
      ax[0,0].plot(t_, x1, 'r')
      ax[0,0].set_title('$x_1(t)$')
      ax[0,1].plot(t_, y1, 'r')
      ax[0,1].set_title('$y_1(t)$')
      ax[0,2].plot(t_, z1, 'r')
      ax[0,2].set_title('$z_1(t)$')
      ax[1,0].plot(t_, x2, 'b')
      ax[1,0].set_title('$x_2(t)$')
      ax[1,1].plot(t_, y2, 'b')
      ax[1,1].set_title('$y_2(t)$')
      ax[1,2].plot(t_, z2, 'b')
      ax[1,2].set_title('$z_2(t)$')

      plt.tight_layout()

      plt.show()
    
    elif option == "v(t)":
      fig, ax = plt.subplots(2, 3, figsize=(15, 10))
      ax[0,0].plot(t_, vx1, 'r')
      ax[0,0].set_title('$v_{x1}(t)$')
      ax[0,1].plot(t_, vy1, 'r')
      ax[0,1].set_title('$v_{y1}(t)$')
      ax[0,2].plot(t_, vz1, 'r')
      ax[0,2].set_title('$v_{z1}(t)$')
      ax[1,0].plot(t_, vx2, 'b')
      ax[1,0].set_title('$v_{x2}(t)$')
      ax[1,1].plot(t_, vy2, 'b')
      ax[1,1].set_title('$v_{y2}(t)$')
      ax[1,2].plot(t_, vz2, 'b')
      ax[1,2].set_title('$v_{z2}(t)$')

      plt.tight_layout()

      plt.show()

    elif option == "a(t)":
      fig, ax = plt.subplots(2, 3, figsize=(15, 10))
      ax[0,0].plot(t_, ax1, 'r')
      ax[0,0].set_title('$a_{x1}(t)$')
      ax[0,1].plot(t_, ay1, 'r')
      ax[0,1].set_title('$a_{y1}(t)$')
      ax[0,2].plot(t_, az1, 'r')
      ax[0,2].set_title('$a_{z1}(t)$')
      ax[1,0].plot(t_, ax2, 'b')
      ax[1,0].set_title('$a_{x2}(t)$')
      ax[1,1].plot(t_, ay2, 'b')
      ax[1,1].set_title('$a_{y2}(t)$')
      ax[1,2].plot(t_, az2, 'b')
      ax[1,2].set_title('$a_{z2}(t)$')

      plt.tight_layout()

      plt.show()

q1 = 1
q2 = -1
m1 = 1
m2 = 1
r1 = np.array([1, 1, 1])
v1 = np.array([1, 2, 5])
r2 = np.array([-1, 10, 5])
v2 = np.array([-1, -2, -5])
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