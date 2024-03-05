from fuerza_lorentz import Lorentz
import numpy as np
import matplotlib.pyplot as plt
if __name__=="__main__":
    r01 = np.array([0,1,1]) #posicion de la partícula 1
    r02 = np.array([0,1,0,]) #posicion de la partícula 2
    m1 = 1.6726e-27 # masa de la partícula 1
    q1 = 1.6e-19 # Carga de la partícula 1
    m2 = 9.1e-31 # Masa de la partícula 2
    q2 = -1.6e-19 # Carga de la partícula 2
    v01 = np.array([1,0,2]) #velocidad inicial de la partícula 1
    v02 = np.array([-1,0,-2]) # Velocidad inicial de la partícula 2
    a01 = np.array([0,0,0]) # Aceleracion inicial de la partícula 1
    a02 = np.array([0,0,0]) # Aceleracion inicial de la partícula 2
    B = np.array([0,0,1]) # Campo magnético
    t = 20
    
    #Creación de las partículas
    particula1 = Lorentz(r01,v01,a01,q1,m1)
    particula2 = Lorentz(r02,v02,a02,q2,m2)
    posicion1 = particula1.posTime(t,particula2,B)
    posicion2 = particula2.posTime(t,particula1,B)
    velocidad1 = particula1.velTime(t,particula2,B)
    velocidad2 = particula2.velTime(t,particula1,B)
    print('-'*12)
    print(posicion1)
    print('-'*12)
    print(posicion2)
    print('-'*12)
    print(velocidad1)
    print('-'*12)
    print(velocidad2)
    particula1.grafica(particula2,t,B)
    #particula2.grafica(particula1,t,B)
    #fig,ax = plt.subplots(1,1)
    #ax.plot()
    
    