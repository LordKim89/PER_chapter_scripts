import numpy as np
from p5 import *
from particle import Particle

class AnimEarth:

    

    def __init__(self, wi, he, frames=366):
        self.frames = frames
        self.w = wi
        self.h = he

        self.sun = Particle(mass=1.989e30)
        self.earth = Particle(init_pos=np.array([150e9, 0], dtype=np.float64), init_vel=np.array([0, 29784.8], dtype=np.float64), mass=5.9721e24)
        moon_vel = np.array([0, 2 * np.pi * 384.4e6 / (28 * 60*60*24)], dtype=np.float64) + self.earth.vel
        self.moon = Particle(init_pos=self.earth.pos+np.array([384.4e6, 0], dtype=np.float64), init_vel=moon_vel, mass=7.34767309e22)

        self.scale_factor = np.linalg.norm(self.moon.pos)*1.1 /(self.w * 0.5)

    def interact(self, p1, p2):
        G = 6.67430e-11
        dl = p1.pos - p2.pos
        dir = np.linalg.norm(dl)
        force_mag = p1.mass * p2.mass * G / (dir**2 + 100)
        force = force_mag * dl/dir
        p1.apply_force(-force)
        p2.apply_force(force)



    def show(self):
        background(255)

        push()

        pop()



        
        
