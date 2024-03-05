import numpy as np
import matplotlib.pyplot as plt


class Particula:
    """Se crea una clase llamada Particula, que cuenta con atributos fijos como masa y carga eléctrica,
       y otros no fijos, como los asociados a la posición, velocidad y aceleración. Además, cuenta con 
       métodos que dan constancia de su dinámica dentro de un campo magnético uniforme, y a la vez, 
       interactuando eléctricamente con otra(s) partícula(s).
       
        Atributos:
                masa: m (float). Representa la masa de la partícula en el kilogramos
                carga: q (float). Representa la carga de la partícula en Coulombs
                posicion inicial: r0 (array). Representa la posición de la partícula m.
                velocidad inicial: v0 (array). Representa la velocidad inicial de la partícula m/s
                aceleracion inicial: a0 (array). Representa la aceleración de la partícula.
        
        Métodos:
                FuerzaLorentz() 
                FuerzaCoulomb()
                FuerzaTotal()
                AceleracionFinal()
                SolNum()
                Graficas()
    """
    def __init__(self, r0, v0, a0, m, q):
      '''Constructor de la clase.
        
        Parámetros:
            r0 (array): posición inicial.
            v0 (array): velocidad inicial.
            a0 (array): Aceleración inicial.
            q (float) : carga de la partícula
            m (float) : masa de la partícula'''
      
      self.posicion = r0
      self.velocidad = v0
      self.aceleracion = a0
      self.masa = m
      self.carga = q
    
    #Método para la fuerza de Lorentz
    def AceleracionLorentz(self, campoB):
      ''' Fuerza magnética: fuerza de interacción magnética mediada por la parte magnética de la fuerza de Lorentz.
        Parámetros:
            - campoB (array): Un campo magnético como vector
            - self : método propio de la partícula
            
        Retorna:
            - arrar: Arreglo de numpy de tres elementos con las componentes de las fuerzas [fx,fy,fz]'''  
      a_L = (1/self.masa)*self.carga * np.cross(self.velocidad, campoB) #Producto vectorial entre v y B (Lorentz)
      
      return a_L #Aceleración debida a la fuerza de Lorentz

    #Método para la fuerza de Coulomb
    def AceleracionCoulomb(self, p2, k = 9e+9):
      '''Fuerza eléctrica: la fuerza de interacción eléctrica mediada por la fuerza de Coulomb.
        Parámetros:
            - self: método propio de la partícula 1
            - Q (float): la carga de la partícula 2
            - posicion2 (array): la posición de la partícula 2
        Retorna:
            - Arreglo de tres elementos con las componentes de la fuerza [Fx,Fy,Fz]'''
      C = k * self.carga* p2.carga #Constante de las cargas
      dir = p2.posicion - self.posicion #Dirección del campo eléctrico
      r = np.sqrt(np.dot(p2.posicion - self.posicion, p2.posicion - self.posicion)) #Magnitud de dirección
      a_C = (C/(self.masa)*r**3)*dir #Aceleración debida a la fuerza de de Coulomb
      
      return a_C
    
    #Método para la fuerza total
    def AceleracionTotal(self):
       ''' Fuerza total: calcula la fuerza de Lorentz para la partícula definida.
        Parámetros:
            - self: como método propio del objeto.
        Retorna:
            - Arreglo de tres elementos con las componentes de la fuerza total.
    
        Aceleración final: calcula la aceleración total de la partícula 
        Parámetros:
            - self: como método propio del objeto
        Retorna:
            - Arreglo de tres elementos con las componente de la aceleración total de la partícula.'''


       a_L = self.AceleracionLorentz(campoB)
       a_C = self.AceleracionCoulomb(p2, k = 9e+9)
       a_T = a_L + a_C
        
       return a_T 
    
    #Método para la solución numérica
    def SolNum(self, t, dt):
        a = self.AceleracionTotal()
        # dt = 0.1
        #T = np.arange(0, t, dt)
        T = np.arange(0, t + dt, dt)
        Posicion = np.zeros((len(T), 3))
        Velocidad = np.zeros((len(T), 3))
        Posicion[0] = self.posicion
        Velocidad[0] = self.velocidad
        
        
        for i in range(len(T)-1):
            Velocidad[i + 1] = Velocidad[i] + a*T[i + 1]
            Posicion[i + 1] = Posicion[i] + Velocidad[i]*T[i + 1] + 0.5*a*(T[i + 1])**2

        return Posicion, Velocidad
    
    def Plots(self, sol, t, dt):
      T = np.arange(0, t + dt, dt)
      sol = self.SolNum(t, dt)
      x = [i[0] for i in sol[0]]
      y = [i[1] for i in sol[0]]
      z = [i[2] for i in sol[0]]

      fig = plt.figure()
      ax = fig.add_subplot(111, projection='3d')
      ax.plot(x, y, z)

      # Etiquetas de los ejes
      ax.set_xlabel('X')
      ax.set_ylabel('Y')
      ax.set_zlabel('Z')
      
      # Mostrar la gráfica
      plt.show()


posicion1 = np.array([0,0,0])
velocidad1 = np.array([1,0,0])
posicion2 = np.array([1,2,0])
velocidad2 = np.array([-1,0,0])
aceleracion=np.zeros(3)

p1 = Particula(posicion1, velocidad1, aceleracion, m = 10, q = 1)
p2 = Particula(posicion2, velocidad2, aceleracion, m = 10, q = -1)
campoB = np.array([1, 0, 0])
#Q = -1
#posicion2 = np.array([-1, 1, 2])

F_L = p1.AceleracionLorentz(campoB)
F_C = p1.AceleracionCoulomb(p2, posicion2)
a= p1.AceleracionTotal()
sol = p1.SolNum(0.5, 0.0001)

#print(sol[0])

p1.Plots(sol, 0.5, 0.0001)