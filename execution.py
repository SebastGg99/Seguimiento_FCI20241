from fuerza_lorentz import Lorentz
from clase import Particle
import numpy as np
import matplotlib.pyplot as plt
if __name__=="__main__":
    v1 = np.array([1, 0, 0])
q1 = 1
m1 = 1
B = np.array([0, 0, 1])
r1 = np.array([1, 0, 1])  # Initial position for particle 1
v2 = np.array([0, 1, 0])  # Initial velocity for particle 2
q2 = 1
m2 = 1
r2 = np.array([1, 1, 0])  # Initial position for particle 2

particle = Particle(v1, q1, m1, B, r1, v2, q2, m2, r2)
particle.plot_motion()
    
    