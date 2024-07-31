import numpy as np
from p5 import *

class Particle:
    def __init__(self, init_pos=np.array([0,0], dtype=np.float64), init_vel=np.array([0,0], dtype=np.float64), mass=1):
        self.pos = init_pos
        self.vel = init_vel
        self.force = np.array([0,0], dtype=np.float64)
        self.mass = mass

    def update(self, dt):
        self.acc = self.force/self.mass
        self.vel += self.acc * dt
        self.pos += self.vel * dt
        self.force = np.array([0,0], dtype=np.float64)

    def apply_force(self, force):
        self.force += force

    

    