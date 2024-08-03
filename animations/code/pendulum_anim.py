import numpy as np
from p5 import *
from particle import Particle
from colors import ColorPicker
import copy

class AnimPendulum:
    def __init__(self, wi, he, frames=500, save_frame=200):
        self.frames = frames
        self.save_frame = save_frame
        self.w = wi
        self.h = he
        self.time = 0
        cp = ColorPicker()
        self.pal = cp.get_palette("GrayRedGreen")
        
        self.center = Particle()
        self.joint_length_1 = self.w/4
        self.joint_1 = Particle(init_pos=copy.copy(self.center.pos + np.array([0, -self.joint_length_1])))
        self.joint_length_2 = self.w/8
        self.joint_2 = Particle(init_pos=copy.copy(self.joint_1.pos + np.array([self.joint_length_2, 0])))

        self.path = [copy.copy(self.joint_2.pos)]


    def show(self):
        background(255)

        push()

        gravity = np.array([0, 10])

        for i in range(40):
            # calculate forces
            self.joint_1.apply_force(gravity)
            self.joint_2.apply_force(gravity)
            k = 1000
            j1c_force_mag = k * (np.linalg.norm(self.center.pos - self.joint_1.pos) - self.joint_length_1)
            j2c_force_mag = k * (np.linalg.norm(self.joint_1.pos - self.joint_2.pos) - self.joint_length_2)

            j1c_dir = (self.center.pos - self.joint_1.pos)/np.linalg.norm(self.center.pos - self.joint_1.pos)
            j2c_dir = (self.joint_1.pos - self.joint_2.pos)/np.linalg.norm(self.joint_1.pos - self.joint_2.pos)

            self.joint_1.apply_force(j1c_dir * j1c_force_mag)
            self.joint_1.apply_force(-j2c_dir * j2c_force_mag)
            self.joint_2.apply_force(j2c_dir * j2c_force_mag)

            dt = 0.01
            # update positions
            
            self.joint_1.update(dt)
            self.joint_2.update(dt)


            self.path.append(copy.copy(self.joint_2.pos))

        # show particles
        translate(self.w*0.5, self.h*0.5)
        stroke_weight(2)
        stroke(self.pal["highlight-line"])
        for i in range(len(self.path) - 1):
            line(self.path[i][0], self.path[i][1], self.path[i+1][0], self.path[i+1][1])


        stroke_weight(10)
        fill(self.pal["dark-area"])
        stroke(self.pal["dark-line"])
        
        line(self.center.pos[0], self.center.pos[1], self.joint_1.pos[0], self.joint_1.pos[1])
        line(self.joint_1.pos[0], self.joint_1.pos[1], self.joint_2.pos[0], self.joint_2.pos[1])
        stroke_weight(5)
        circle(self.center.pos[0], self.center.pos[1], 30)
        circle(self.joint_1.pos[0], self.joint_1.pos[1], 20)
        circle(self.joint_2.pos[0], self.joint_2.pos[1], 20)

   



        pop()

        self.time += 1/60


