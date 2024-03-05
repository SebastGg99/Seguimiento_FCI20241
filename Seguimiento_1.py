import numpy as np

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

<<<<<<< HEAD
    #masa = 10
    #carga = 1
    # posicion = np.zeros(3)
    # velocidad = np.zeros(3)
    #aceleracion = np.zeros(3)

    def __init__(self, t, dt, r0, v0, a0, m, q):
        '''
=======
    def __init__(self, r0, v0, a0, m, q):
      '''
>>>>>>> 52bdd595ff1a533a9ef9a1d81c075f913f721e98
        Constructor de la clase.
        
        Parámetros:
            r0 (array): posición inicial.
            v0 (array): velocidad inicial.
            a0 (array): Aceleración inicial.
            q (float) : carga de la partícula
            m (float) : masa de la partícula'''
<<<<<<< HEAD
        
        self.tiempo = np.arange(0, t, dt)
        self.posicion = np.zeros((len(self.tiempo), 3))
        self.posicion[0] = r0
        self.velocidad = np.zeros((len(self.tiempo), 3))
        self.velocidad[0] = v0
        self.aceleracion = np.zeros((len(self.tiempo), 3))
        self.aceleracion[0] = a0
        self.masa = m
        self.carga = q
=======
      self.posicion[0] = r0
      self.velocidad[0] = v0
      self.aceleracion[0] = a0
      self.masa = m
      self.carga = q
>>>>>>> 52bdd595ff1a533a9ef9a1d81c075f913f721e98
    
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
<<<<<<< HEAD
    def FuerzaCoulomb(self, particula2, k = 9e+9):
        '''Fuerza eléctrica: la fuerza de interacción eléctrica mediada por la fuerza de Coulomb.
=======
    def AceleracionCoulomb(self, Q, p2, k = 9e+9):
      '''Fuerza eléctrica: la fuerza de interacción eléctrica mediada por la fuerza de Coulomb.
>>>>>>> 52bdd595ff1a533a9ef9a1d81c075f913f721e98
        Parámetros:
            - self: método propio de la partícula 1
            - Q (float): la carga de la partícula 2
            - posicion2 (array): la posición de la partícula 2
        Retorna:
            - Arreglo de tres elementos con las componentes de la fuerza [Fx,Fy,Fz]'''
<<<<<<< HEAD
        C = k * self.carga * particula2.carga #Constante de las cargas
        dir = particula2.posicion - self.posicion #Dirección del campo eléctrico
        r = np.sqrt(np.dot(particula2.posicion - self.posicion, 
                           particula2.posicion - self.posicion)) #Magnitud de dirección
        F_C = (C/r**3)*dir #Fuerza de Coulomb
=======
      C = k*self.carga*Q #Constante de las cargas
      posicion2 = p2.posicion[0]
      dir = self.posicion - p2.posicion #Dirección del campo eléctrico
      r = np.sqrt(np.dot(self.posicion - p2.posicion, self.posicion - p2.posicion)) #Magnitud de dirección
      a_C = (C/(self.masa)*r**3)*dir #Aceleración debida a la fuerza de de Coulomb
      
      return a_C
        
>>>>>>> 52bdd595ff1a533a9ef9a1d81c075f913f721e98
            
        

    
    #Método para la fuerza total
    def AceleracionTotal(self):
<<<<<<< HEAD
        ''' Fuerza total: calcula la fuerza de Lorentz para la partícula definida.
=======
    ''' Fuerza total: calcula la fuerza de Lorentz para la partícula definida.
>>>>>>> 52bdd595ff1a533a9ef9a1d81c075f913f721e98
        Parámetros:
            - self: como método propio del objeto.
        Retorna:
            - Arreglo de tres elementos con las componentes de la fuerza total.'''
<<<<<<< HEAD
        F_L = self.FuerzaLorentz(campoB)
        F_C = self.FuerzaCoulomb(particula2, k = 9e+9)

        F_T = F_L + F_C #Fuerza total
        a_T = F_T / self.masa #Aceleración total
        return a_T
    
    #Método para la aceleración final
    # def AceleracionFinal(self):
    #     '''Aceleración final: calcula la aceleración total de la partícula 
    #     Parámetros:
    #         - self: como método propio del objeto
    #     Retorna:
    #         - Arreglo de tres elementos con las componente de la aceleración total de la partícula.'''
    #     F_T = self.FuerzaTotal()
    #     a = F_T / self.masa

    #     return a
=======
    
    '''Aceleración final: calcula la aceleración total de la partícula 
        Parámetros:
            - self: como método propio del objeto
        Retorna:
            - Arreglo de tres elementos con las componente de la aceleración total de la partícula.'''
        a_L = self.AceleracionLorentz(campoB)
        a_C = self.AceleracionCoulomb(Q, p2.posicion, k = 9e+9)
        a_T = a_L + a_C
        
        return a_T 
>>>>>>> 52bdd595ff1a533a9ef9a1d81c075f913f721e98
    
    #Método para la solución numérica
    def SolNum(self):
        a = self.AceleracionTotal()
        # dt = 0.1
        #T = np.arange(0, t, dt)
<<<<<<< HEAD
        #T = np.arange(0, t + dt, dt)
        #Posicion = np.zeros((len(T), 3))
        #Velocidad = np.zeros((len(T), 3))
        #Posicion[0] = self.posicion
        #Velocidad[0] = self.velocidad

        for i in range(len(self.tiempo)):
            self.velocidad[i+1] = self.velocidad[i] + a * self.tiempo[i + 1]
            self.posicion[i+1] = self.posicion[i] + self.velocidad[i] * self.tiempo[i+1] 
            + 0.5 * a * (self.tiempo[i+1])**2

        return self.posicion, self.velocidad
=======
        T = np.arange(0, t + dt, dt)
        # Posicion = np.zeros((len(T), 3))
        # Velocidad = np.zeros((len(T), 3))
        # Posicion[0] = self.posicion
        # Velocidad[0] = self.velocidad
        
        
        for i in range(len(T)):
            Velocidad[i + 1] = Velocidad[i] + a*T[i + 1]
            Posicion[i + 1] = Posicion[i] + Velocidad[i]*t[i + 1] + 0.5*a*(t[i + 1])**2
>>>>>>> 52bdd595ff1a533a9ef9a1d81c075f913f721e98


posicion1 = np.array([0,0,0])
velocidad1 = np.array([1,0,0])
posicion2 = np.array([1,2,0])
velocidad2 = np.array([-1,0,0])
aceleracion=np.zeros(3)

<<<<<<< HEAD
p1 = Particula(10, 0.1, posicion1, velocidad1, aceleracion, m = 10, q = 1)
particula2 = Particula(10, 0.1, posicion2, velocidad2, aceleracion, m = 10, q = -1)
=======
p = Particula(posicion, velocidad, np.zeros(3), m = 10, q = 1)
>>>>>>> 52bdd595ff1a533a9ef9a1d81c075f913f721e98
campoB = np.array([2, 1, 5])
#Q = -1
#posicion2 = np.array([-1, 1, 2])

<<<<<<< HEAD
F_L = p1.FuerzaLorentz(campoB)
F_C = p1.FuerzaCoulomb(particula2)
a = p1.AceleracionTotal()
sol = p1.SolNum()
=======
F_L = p.FuerzaLorentz(campoB)
F_C = p.FuerzaCoulomb(Q, posicion2)
F_T = p.FuerzaTotal()
a = p.AceleracionFinal()
sol = p.SolNum(10,0.1)
>>>>>>> 52bdd595ff1a533a9ef9a1d81c075f913f721e98

print(sol[0])