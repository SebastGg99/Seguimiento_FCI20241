import numpy as np

class Particula:
    """Se crea una clase llamada Particula, que cuenta con atributos fijos como masa y carga eléctrica,
       y otros no fijos, como los asociados a la posición, velocidad y aceleración. Además, cuenta con 
       métodos que dan constancia de su dinámica dentro de un campo magnético uniforme, y a la vez, 
       interactuando eléctricamente con otra(s) partícula(s).
       
        Atributos:
                masa: m
                carga: q
                posicion inicial: r0
                velocidad inicial: v0
                aceleracion inicial: a0
        
        Métodos:
                FuerzaLorentz()
                FuerzaCoulomb()
                FuerzaTotal()
                AceleracionFinal()
                SolNum()
    """

    def __init__(self, r0, v0, a0, m, q):
        self.posicion[0] = r0
        self.velocidad[0] = v0
        self.aceleracion[0] = a0
        self.masa = m
        self.carga = q
    
    #Método para la fuerza de Lorentz
    def AceleracionLorentz(self, campoB):
        a_L = (1/self.masa)*self.carga * np.cross(self.velocidad, campoB) #Producto vectorial entre v y B (Lorentz)
        return a_L #Aceleración debida a la fuerza de Lorentz

    #Método para la fuerza de Coulomb
    def AceleracionCoulomb(self, Q, r02, k = 9e+9):
        C = k*self.carga*Q #Constante de las cargas
        r02 = p2.posicion[0]
        dir = self.posicion - p2.posicion #Dirección del campo eléctrico
        r = np.sqrt(np.dot(self.posicion - p2.posicion, self.posicion - p2.posicion)) #Magnitud de dirección
        a_C = (C/(self.masa)*r**3)*dir #Aceleración debida a la fuerza de de Coulomb
            
        return a_C

    
    #Método para la fuerza total
    def AceleracionTotal(self):
        a_L = self.AceleracionLorentz(campoB)
        a_C = self.AceleracionCoulomb(Q, p2.posicion, k = 9e+9)

        a_T = a_L + a_C
        return a_T
    
    #Método para la aceleración final
    def AceleracionFinal(self):
        F_T = self.FuerzaTotal()
        a = F_T / self.masa

        return a
    
    #Método para la solución numérica
    def SolNum(self, t, dt):
        a = self.AceleracionFinal()
        # dt = 0.1
        #T = np.arange(0, t, dt)
        T = np.arange(0, t + dt, dt)
        # Posicion = np.zeros((len(T), 3))
        # Velocidad = np.zeros((len(T), 3))
        # Posicion[0] = self.posicion
        # Velocidad[0] = self.velocidad
        
        
        for i in range(len(T)):
            Velocidad[i + 1] = Velocidad[i] + a*T[i + 1]
            Posicion[i + 1] = Posicion[i] + Velocidad[i]*t[i + 1] + 0.5*a*(t[i + 1])**2


posicion = np.array([3,1,2])
velocidad = np.array([0,0,0])

p = Particula(posicion, velocidad, np.zeros(3), m = 10, q = 1)
campoB = np.array([2, 1, 5])
Q = -1
posicion2 = np.array([-1, 1, 2])

F_L = p.FuerzaLorentz(campoB)
F_C = p.FuerzaCoulomb(Q, posicion2)
F_T = p.FuerzaTotal()
a = p.AceleracionFinal()
sol = p.SolNum(10,0.1)



#######PRUEBAS#######

#print(f"La fuerza de Lorentz es: {F_L}")
# print(f"La fuerza de Coulomb es: {F_C}")
# print(f"La fuerza total es: {F_T}")
# print(f"La aceleración es: {a}")
#print(sol)