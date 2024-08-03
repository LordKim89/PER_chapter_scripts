import numpy as np
from p5 import *
from particle import Particle
from colors import ColorPicker
import copy

class AnimCloth:
    def __init__(self, wi, he, frames=150, save_frame=145):
        self.frames = frames
        self.save_frame = save_frame
        self.w = wi
        self.h = he
        self.time = 0
        cp = ColorPicker()
        self.pal = cp.get_palette("GrayRedGreen")
        
        self.p_w = 20
        self.p_h = 30
        self.dx = self.w * 0.8/(self.p_w - 1)
        self.dy = self.h * 0.6/(self.p_h - 1)
        self.particles = [[None for _ in range(self.p_h)] for _ in range(self.p_w)]
        for x in range(self.p_w):
            for y in range(self.p_h):
                pos = np.array([x * self.dx + self.w*0.1, y * self.dy + self.h*0.1])
                self.particles[x][y] = Particle(init_pos=pos)


       



    def show(self):
        background(255)

        push()

        gravity = np.array([0, 10])
        k = 1000
    
        for _ in range(20):
            
            for x in range(self.p_w):
                for y in range(self.p_h):

                    force = np.array([0,0], dtype=np.float64)
                    if x > 0:
                        dv = self.particles[x][y].pos - self.particles[x-1][y].pos
                        dl = np.linalg.norm(dv)
                        dir = -dv/(dl + 1)
                        force += dir * k * (dl - self.dx)

                    if y > 0:
                        dv = self.particles[x][y].pos - self.particles[x][y-1].pos
                        dl = np.linalg.norm(dv)
                        dir = -dv/(dl + 1)
                        force += dir * k * (dl - self.dy)

                    if x < self.p_w - 1:
                        dv = self.particles[x][y].pos - self.particles[x+1][y].pos
                        dl = np.linalg.norm(dv)
                        dir = -dv/(dl + 1)
                        force += dir * k * (dl - self.dx)

                    if y < self.p_h - 1:
                        dv = self.particles[x][y].pos - self.particles[x][y+1].pos
                        dl = np.linalg.norm(dv)
                        dir = -dv/(dl + 1)
                        force += dir * k * (dl - self.dy)

                    self.particles[x][y].apply_force(force)
                    self.particles[x][y].apply_force(gravity)
                    self.particles[x][y].apply_force(-0.2 * self.particles[x][y].vel)


            dt = 0.01
            for x in range(self.p_w):
                for y in range(self.p_h):
                    
                    if not ((x == 0 or x == self.p_w - 1) and y == 0):
                        self.particles[x][y].update(dt)


        
                # show
        stroke(self.pal["light-line"])
        stroke_weight(2)
        for x in range(self.p_w):
            for y in range(self.p_h):
                if x > 0:
                    line(self.particles[x][y].pos[0], self.particles[x][y].pos[1], self.particles[x-1][y].pos[0], self.particles[x-1][y].pos[1])

                if y > 0:
                    line(self.particles[x][y].pos[0], self.particles[x][y].pos[1], self.particles[x][y-1].pos[0], self.particles[x][y-1].pos[1])

                if x < self.p_w - 1:
                    line(self.particles[x][y].pos[0], self.particles[x][y].pos[1], self.particles[x+1][y].pos[0], self.particles[x+1][y].pos[1])

                if y < self.p_h - 1:
                    line(self.particles[x][y].pos[0], self.particles[x][y].pos[1], self.particles[x][y+1].pos[0], self.particles[x][y+1].pos[1])

        no_stroke()
        for x in range(self.p_w):
            for y in range(self.p_h):
                fill(self.pal["highlight-line"])
                circle(self.particles[x][y].pos[0], self.particles[x][y].pos[1], 5)

        pop()


        self.time += 1/60


