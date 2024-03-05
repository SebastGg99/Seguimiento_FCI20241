import numpy as np
import matplotlib.pyplot as plt
class Lorentz:
    '''
    Clase para representar una partícula que experimenta fuerzas magnéticas y eléctricas en un campo.
    '''
    r = []
    v = []
    a0 = [0,0,0]

    def __init__(self, r0, v0, a0, q, m):
        '''
        Constructor de la clase.

        Parámetros:
        - r0 (array): Posición inicial de la partícula en forma de un arreglo numpy de 3 elementos [x, y, z].
        - v (array): Velocidad inicial de la partícula en forma de un arreglo numpy de 3 elementos [vx, vy, vz].
        - a0 (array): Aceleración inicial de la partícula en forma de un arreglo numpy de 3 elementos [ax, ay, az].
        - q (float): Carga de la partícula en Coulombs.
        - m (float): Masa de la partícula en kilogramos.
        '''
        self.m = m  # Masa en kilogramos
        self.q = q  # Carga en Coulombs
        self.r0 = r0  # Posición de la partícula
        self.v0 = v0  # Velocidad de la partícula m/s
        self.a0 = a0  # Aceleración inicial de la partícula


    # Aceleración iniciales
    def aMagnetic(self,B):
        '''
        Calcula la aceleración debida al campo magnético.

        Parámetros:
        - B (array): Campo magnético en forma de un arreglo numpy de 3 elementos [Bx, By, Bz].

        Retorna:
        - array: Arreglo numpy de 3 elementos [ax, ay, az] representando la aceleración en cada dirección.
        '''
        ax = (self.q / self.m) * (self.v0[1] * B[2] - self.v0[2] * B[1])
        ay = -(self.q / self.m) * (self.v0[0] * B[2] - self.v0[2] * B[0])
        az = (self.q / self.m) * (self.v0[0] * B[1] - self.v0[1] * B[0])
        return np.array([ax, ay, az])

    def aElectric(self, particula2):
        '''
        Calcula la aceleración debida a la interacción eléctrica con otra partícula cargada.

        Parámetros:
        - particula2 (Lorentz): Objeto de la clase Lorentz que representa la otra partícula.

        Retorna:
        - array: Arreglo numpy de 3 elementos [ax, ay, az] representando la aceleración en cada dirección.
        '''
        q1 = self.q
        q2 = particula2.q
        m1 = self.m
        r1 = np.array(self.r0)
        r2 = np.array(particula2.r0)
        K = 9e9  # Constante de campo eléctrico
        distance = np.linalg.norm(r2 - r1)
        if distance == 0:
            print("Las partículas están en la misma posición")
            return self.a0
        else:
            ax = (K / m1) * (q1 * q2) * (r2[0] - r1[0]) / distance**3
            ay = (K / m1) * (q1 * q2) * (r2[1] - r1[1]) / distance**3
            az = (K / m1) * (q1 * q2) * (r2[2] - r1[2]) / distance**3
            return np.array([ax, ay, az])

    def aTotal(self,particula2,B):
        ae = self.aElectric(particula2)
        am = self.aMagnetic(B)

        return ae+am
    
    # Evolucion temporal de la posicion y la velocidad
    def posTime(self,t,particula2,B):
        r = self.r
        for i in range(0,t):
            r.append(self.r0+ self.v0*i +(0.5)*self.aTotal(particula2,B)*(i**2))
        return np.array(r)
    
    def velTime(self,t,particula2, B):
        v = self.v
        v = self.v0+ self.aTotal(particula2,B)*t
        return v
    
    
    
    

