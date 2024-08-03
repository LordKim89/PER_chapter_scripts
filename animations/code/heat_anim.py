import numpy as np
from p5 import *
from particle import Particle
from colors import ColorPicker
import copy

class AnimHeat:
    def __init__(self, wi, he, frames=120, save_frame=40):
        self.frames = frames
        self.save_frame = save_frame
        self.w = wi
        self.h = he
        self.time = 0
        cp = ColorPicker()
        self.pal = cp.get_palette("GrayRedGreen")
        
        self.p_w = 50
        self.p_h = 50
        self.dx = self.w * 0.8/(self.p_w - 1)
        self.dy = self.h * 0.8/(self.p_h - 1)
        self.particles = [[None for _ in range(self.p_h)] for _ in range(self.p_w)]
        for x in range(self.p_w):
            for y in range(self.p_h):
                pos = np.array([x * self.dx + self.w*0.1, y * self.dy + self.h*0.1])
                self.particles[x][y] = Particle(init_pos=pos)
                self.particles[x][y].temperature = 10
                self.particles[x][y].dT = 0
                self.particles[x][y].mugged = False

       
        self.mug_temp = 300



    def show(self):
        background(255)

        push()


        C = 10
        for n in range(20):
            
            for x in range(1, self.p_w - 1):
                for y in range(1, self.p_h - 1):

                    dl = np.linalg.norm(self.particles[x][y].pos - np.array([self.w*0.5, self.h*0.5]))
                    #print(np.abs(dl - self.w * 0.3))
                    self.particles[x][y].mugged = False
                    if np.abs(dl - self.w*0.2) < self.dx*1 and self.time < 1:
                        self.particles[x][y].dT += C * (self.mug_temp - self.particles[x][y].temperature)
                        self.particles[x][y].mugged = True                   
                    
                    
                    dT = 0
                    dT += self.particles[x-1][y].temperature - self.particles[x][y].temperature
                    dT += self.particles[x+1][y].temperature - self.particles[x][y].temperature
                    dT += self.particles[x][y-1].temperature - self.particles[x][y].temperature
                    dT += self.particles[x][y+1].temperature - self.particles[x][y].temperature
                    self.particles[x][y].dT += dT * C

            dt = 1/60
            for x in range(self.p_w):
                for y in range(self.p_h):
                    self.particles[x][y].temperature += self.particles[x][y].dT * dt
                    self.particles[x][y].dT = 0


        
                # show
        no_stroke()
        for x in range(self.p_w):
            for y in range(self.p_h):
                lf = lerp(0, 1, self.particles[x][y].temperature/200)
                cr = (200 * lf + 30) * (1 - self.particles[x][y].mugged)
                cg = (10) * (1 - self.particles[x][y].mugged)
                cb = (10 * (1 - lf) + 30) * (1 - self.particles[x][y].mugged)
                fill(cr, cg, cb)
                rect(self.particles[x][y].pos[0], self.particles[x][y].pos[1], self.dx*1.01, self.dy*1.01)





        pop()

        self.time += 1/60


