import numpy as np
from p5 import *
from particle import Particle
from colors import ColorPicker
import copy

class AnimHunter:

    

    def __init__(self, wi, he, frames=68):
        self.frames = frames
        self.w = wi
        self.h = he
        cp = ColorPicker()
        self.pal = cp.get_palette("GrayRedGreen")
        m_pos = np.array([self.w*0.9, self.h*0.1])
        self.monkey = Particle(init_pos=m_pos)
        b_pos = np.array([self.w*0.1, self.h*0.9])
        b_vel = (m_pos - b_pos) * 0.15
        self.bullet = Particle(init_pos=b_pos, init_vel=b_vel)

        self.b_path = [copy.copy(self.bullet.pos)]
        self.m_path = [copy.copy(self.monkey.pos)]



    def show(self):
        background(255)

        dt = 0.1

        gravity = np.array([0, 10])

        self.monkey.apply_force(gravity)
        self.bullet.apply_force(gravity)
        self.monkey.update(dt)
        self.bullet.update(dt)

        self.b_path.append(copy.copy(self.bullet.pos))
        self.m_path.append(copy.copy(self.monkey.pos))


        push()
        
        # draw monkey
        fill(self.pal["basic-area"])
        stroke(self.pal["basic-line"])
        stroke_weight(5)
        circle(self.monkey.pos[0], self.monkey.pos[1], 30)
        stroke_weight(5)
        for l in range(len(self.m_path) - 1):
            line(self.m_path[l][0], self.m_path[l][1], self.m_path[l+1][0], self.m_path[l+1][1])

        # draw bullet
        fill(self.pal["highlight-area"])
        stroke(self.pal["highlight-line"])
        stroke_weight(5)
        circle(self.bullet.pos[0], self.bullet.pos[1], 10)
        stroke_weight(2)
        for l in range(len(self.b_path) - 1):
            line(self.b_path[l][0], self.b_path[l][1], self.b_path[l+1][0], self.b_path[l+1][1])

        pop()



        
        
