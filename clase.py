import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, q1, m1, r1, v1, q2, m2, r2, v2, t_end=30, num_steps=200):
        """
        Inicializa las características de las partículas y los parámetros de simulación.

        Parámetros:
        - q1: Carga de la primera partícula.
        - m1: Masa de la primera partícula.
        - r1: Posición inicial de la primera partícula como un array [x1, y1, z1].
        - v1: Velocidad inicial de la primera partícula como un array [vx1, vy1, vz1].
        - q2: Carga de la segunda partícula.
        - m2: Masa de la segunda partícula.
        - r2: Posición inicial de la segunda partícula como un array [x2, y2, z2].
        - v2: Velocidad inicial de la segunda partícula como un array [vx2, vy2, vz2].
        - t_end: Tiempo final de la simulación en unidades de tiempo.
        - num_steps: Número de pasos de tiempo para la simulación.
        """
        self.q1 = q1
        self.m1 = m1
        self.r1 = r1
        self.v1 = v1
        self.q2 = q2
        self.m2 = m2
        self.r2 = r2
        self.v2 = v2
        self.t_end = t_end
        self.num_steps = num_steps

    def motion(self, B):
        """
        Calcula las trayectorias de las partículas bajo la influencia de campos magnéticos e interacción
        Coulombiana.

        Parámetros:
        - B: Campo magnético como un array [Bx, By, Bz].

        Retorna:
        - r1: Trayectoria de la primera partícula como un array de tamaño (num_steps, 3).
        - v1: Velocidad de la primera partícula como un array de tamaño (num_steps, 3).
        - a1: Aceleración de la primera partícula como un array de tamaño (num_steps, 3).
        - r2: Trayectoria de la segunda partícula como un array de tamaño (num_steps, 3).
        - v2: Velocidad de la segunda partícula como un array de tamaño (num_steps, 3).
        - a2: Aceleración de la segunda partícula como un array de tamaño (num_steps, 3).
        """
        def aMagnetic(v, q, m):
            """
            Calcula la aceleración experimentada por una partícula cargada en un campo magnético.
            
            Parámetros:
                - v: Velocidad de la partícula.
                - q: Carga de la partícula.
                - m: Masa de la partícula.
                
            Retorna:
                - np.array: La aceleración magnética como un vector numpy.
            """
            return (q/m)*np.cross(v, B) #Retorna la aceleración de Lorentz
        
        def aElectric(r1, r2, q1, q2, m, k=1):
            """
            Calcula la aceleración eléctrica experimentada por una partícula cargada en presencia de 
            otra partícula cargada.
            
            Parámetros:
                - r1: Posición de la primera partícula.
                - r2: Posición de la segunda partícula.
                - q1: Carga de la primera partícula.
                - q2: Carga de la segunda partícula.
                - m: Masa de la partícula.
                - k: Constante de Coulomb (por defecto 1).
                
            Retorna:
                - np.array: La aceleración eléctrica como un vector numpy.
            """
            #Definimos la distancia y dirección entre las partículas
            distance = np.linalg.norm(r2 - r1)
            direction = (r2 - r1)/distance
            return (k/m)* q1*q2*direction /distance**2 #Retorna la aceleración de Coulomb
        
        t = np.linspace(0, self.t_end, self.num_steps) #Creamos el tiempo de integración

        #Creamos la matriz de posiciones, velocidades y aceleraciones
        r1 = np.zeros((len(t),3))
        r2 = np.zeros((len(t),3))
        v1 = np.zeros((len(t),3))
        v2 = np.zeros((len(t),3))
        a1 = np.zeros((len(t),3))
        a2 = np.zeros((len(t),3))
        
        #Indicamos las condiciones iniciales de ambas partículas
        v1[0] = self.v1
        r1[0] = self.r1
        v2[0] = self.v2
        r2[0] = self.r2

        for i in range(1, len(t)):
            #Se realiza la iteración, actualizando aceleración, velocidad y posición de la partícula...
            a_magnetic1 = aMagnetic(v1[i-1], self.q1, self.m1)
            a_electric1 = aElectric(r1[i-1], r2[i-1], self.q1, self.q2, self.m1)
            a_total1 = a_magnetic1 + a_electric1
            v1[i] = v1[i-1] + a_total1 * (t[i] - t[i-1])
            r1[i] = r1[i-1] + v1[i-1] * (t[i] - t[i-1]) + 0.5 * a_total1 * (t[i] - t[i-1])**2
            a1[i] = a_total1

            #... Se hace lo mismo para la segunda partícula
            a_magnetic2 = aMagnetic(v2[i-1], self.q2, self.m2)
            a_electric2 = aElectric(r2[i-1], r1[i-1], self.q2, self.q1, self.m2)
            a_total2 = a_magnetic2 + a_electric2
            v2[i] = v2[i-1] + a_total2 * (t[i] - t[i-1])
            r2[i] = r2[i-1] + v2[i-1] * (t[i] - t[i-1]) + 0.5 * a_total2 * (t[i] - t[i-1])**2
            a2[i] = a_total2

        return r1, v1, a1, r2, v2, a2
    
    def plot_motion(self, B, option = "Trayectorias"):
        """
        Grafica las trayectorias, velocidades y aceleraciones de las partículas.

        Parámetros:
        - B: Campo magnético como un array de 3 elementos [Bx, By, Bz].
        - option: Opción para el tipo de gráfico a mostrar. Puede ser "Trayectorias", "r(t)", "v(t)" 
                  o "a(t)".
        """
        #Definimos las variables que se graficarán, y también el tiempo de las gráficas
        r1, v1, a1, r2, v2, a2 = self.motion(B)
        t = np.linspace(0,self.t_end,self.num_steps)
        
        #Definimos el condicional y las matrices de gráficas para cada valor del parámetro option.
        if option == "Trayectorias":
            fig, ax = plt.subplots(1,3,figsize=(16,5),subplot_kw={'projection':'3d'})
            # Position graphs
            ax[0].plot(r1[:, 0], r1[:, 1], r1[:, 2],'b', label='Particle 1 Position')
            ax[0].plot(r2[:, 0], r2[:, 1], r2[:, 2], 'r', label='Particle 2 Position')
            ax[0].set_xlabel('X')
            ax[0].set_ylabel('Y')
            ax[0].set_zlabel('Z')
            ax[0].set_title('Position in 3D')
            
            # Velocity graphs
            ax[1].plot(v1[:, 0], v1[:, 1], v1[:, 2],'b', label='Particle 1 Velocity')
            ax[1].plot(v2[:, 0], v2[:, 1], v2[:, 2], 'r', label='Particle 2 Velocity')
            ax[1].set_xlabel('X')
            ax[1].set_ylabel('Y')
            ax[1].set_zlabel('Z')
            ax[1].set_title('Velocity in 3D')
            
            # Acceleration graphs
            ax[2].plot(a1[:, 0], a1[:, 1], a1[:, 2],'b', label='Particle 1 Acceleration')
            ax[2].plot(a2[:, 0], a2[:, 1], a2[:, 2], 'r', label='Particle 2 Acceleration')
            ax[2].set_xlabel('X')
            ax[2].set_ylabel('Y')
            ax[2].set_zlabel('Z')
            ax[2].set_title('Acceleration in 3D')
            
            fig.suptitle('Gráficas 3D')
            plt.savefig('./Graficas3d.jpg')

        elif option == "r(t)":
            fig, ax = plt.subplots(2, 3, figsize=(15, 10))
            ax[0,0].plot(t, r1[:, 0], 'r')
            ax[0,0].set_title('$x_1(t)$')
            ax[0,1].plot(t, r1[:, 1], 'r')
            ax[0,1].set_title('$y_1(t)$')
            ax[0,2].plot(t, r1[:, 2], 'r')
            ax[0,2].set_title('$z_1(t)$')
            ax[1,0].plot(t, r2[:, 0], 'b')
            ax[1,0].set_title('$x_2(t)$')
            ax[1,1].plot(t, r2[:, 1], 'b')
            ax[1,1].set_title('$y_2(t)$')
            ax[1,2].plot(t, r2[:, 2], 'b')
            ax[1,2].set_title('$z_2(t)$')
            
            fig.suptitle('Posiciones 2D')
            plt.subplots_adjust(hspace=0.5)
            plt.savefig('./Posiciones2d.jpg')
            
        
        elif option == "v(t)":
            fig, ax = plt.subplots(2, 3, figsize=(15, 10))
            ax[0,0].plot(t, v1[:, 0], 'r')
            ax[0,0].set_title('$v_{x1}(t)$')
            ax[0,1].plot(t, v1[:, 1], 'r')
            ax[0,1].set_title('$v_{y1}(t)$')
            ax[0,2].plot(t, v1[:, 2], 'r')
            ax[0,2].set_title('$v_{z1}(t)$')
            ax[1,0].plot(t, v2[:, 0], 'b')
            ax[1,0].set_title('$v_{x2}(t)$')
            ax[1,1].plot(t, v2[:, 1], 'b')
            ax[1,1].set_title('$v_{y2}(t)$')
            ax[1,2].plot(t, v2[:, 2], 'b')
            ax[1,2].set_title('$v_{z2}(t)$')
            
            fig.suptitle('Velocidades 2D')
            plt.subplots_adjust(hspace=0.5)
            plt.savefig('./Velocidades2d.jpg')

        elif option == "a(t)":
            fig, ax = plt.subplots(2, 3, figsize=(15, 10))
            ax[0,0].plot(t, a1[:, 0], 'r')
            ax[0,0].set_title('$a_{x1}(t)$')
            ax[0,1].plot(t, a1[:, 1], 'r')
            ax[0,1].set_title('$a_{y1}(t)$')
            ax[0,2].plot(t, a1[:, 2], 'r')
            ax[0,2].set_title('$a_{z1}(t)$')
            ax[1,0].plot(t, a2[:, 0], 'b')
            ax[1,0].set_title('$a_{x2}(t)$')
            ax[1,1].plot(t, a2[:, 1], 'b')
            ax[1,1].set_title('$a_{y2}(t)$')
            ax[1,2].plot(t, a2[:, 2], 'b')
            ax[1,2].set_title('$a_{z2}(t)$')
            
            fig.suptitle('Aceleraciones 2D')
            plt.subplots_adjust(hspace=0.5)
            plt.savefig('./Aceleraciones2d.jpg')