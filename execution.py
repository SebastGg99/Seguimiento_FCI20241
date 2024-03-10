from clase import Particle
import numpy as np
import matplotlib.pyplot as plt

if __name__=="__main__":
    v1 = np.array([1, -1, 0])
    q1 = 1
    m1 = 1
    B = np.array([0, 0, 1])
    r1 = np.array([1, 0, 1])  # Initial position for particle 1
    v2 = np.array([-1, 1, 0])  # Initial velocity for particle 2
    q2 = 1
    m2 = 1
    r2 = np.array([1, 1, 0])  # Initial position for particle 2
    particle = Particle(q1, m1, r1, v1, q2, m2, r2, v2) #q1,m1,r1,v1,q2,m2,r2,v2
    particle.plot_motion(B)
    particle.plot_motion(B, "r(t)")
    particle.plot_motion(B, "v(t)")
    particle.plot_motion(B, "a(t)")
    