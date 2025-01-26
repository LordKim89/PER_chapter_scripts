import numpy as np
from p5 import *
from .particle import Particle
from .colors import ColorPicker
import copy

class AnimWave:
    def __init__(self, wi, he, frames=200, palette="GrayRedGreen"):
        self.frames = frames
        self.save_frame = 150
        self.w = wi
        self.h = he
        self.time = 0
        cp = ColorPicker()
        self.pal = cp.get_palette(palette)
        self.particles = []
        self.nr_of_particles = 100
        dl = self.w*0.8/(self.nr_of_particles-1)
        for k in range(self.nr_of_particles):
           
            pos = np.array([self.w * 0.1 + k*dl, self.h/2], dtype=np.float64)
            self.particles.append(Particle(init_pos=pos))


    def show(self):
        background(255)

        push()

        if self.time == 10/60:
            for i in range(2):
                self.particles[self.nr_of_particles//2 + i].apply_force(np.array([0, 5000]))
                self.particles[self.nr_of_particles//2 - i].apply_force(np.array([0, 5000]))
            #self.particles[self.nr_of_particles//2].apply_force(np.array([0, 10000]))
            #self.particles[self.nr_of_particles//2 -1]
            #for i in range(self.nr_of_particles):
            #    self.particles[i].apply_force(np.array([0, np.sin(i/(self.nr_of_particles*self.w*0.8)*np.pi)])*10000)

        # calculate forces
        for i, p in enumerate(self.particles):
            if i > 0 and i < self.nr_of_particles-1:
                pm = self.particles[i-1]
                pp = self.particles[i+1]
                force = np.array([0, (pm.pos[1] - p.pos[1]) + (pp.pos[1] - p.pos[1])])*50
                p.apply_force(force)
                #p.apply_force(np.array([0, (self.h*0.5 - p.pos[1])]))
                #pm.apply_force(-force)
                #pp.apply_force(-force)
                #p.apply_force(-p.vel*0.01)

        dt = 0.1
        # update positions
        for i in range(1, self.nr_of_particles-1):
            self.particles[i].update(dt)

        # show particles
        stroke_weight(5)
        for i, p in enumerate(self.particles):
            if i < self.nr_of_particles-1:
                line(p.pos[0], p.pos[1], self.particles[i+1].pos[0], self.particles[i+1].pos[1])


        pop()

        self.time += 1/60


