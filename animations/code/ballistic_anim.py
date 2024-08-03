import numpy as np
from p5 import *
from particle import Particle
from colors import ColorPicker
import copy

class AnimBallistic:

    

    def __init__(self, wi, he, frames=150, save_frame=100):
        self.frames = frames
        self.save_frame = save_frame
        self.w = wi
        self.h = he
        cp = ColorPicker()
        self.pal = cp.get_palette("GrayRedGreen")
        m_pos = np.array([self.w*0.9, -self.h*1])
        self.target = Particle(init_pos=m_pos)
        b_pos = np.array([self.w*0.1, self.h*0.9])
        b_vel = (m_pos - b_pos) * 0.10
        self.bullet_1 = Particle(init_pos=b_pos, init_vel=b_vel)
        self.b1_path = [copy.copy(self.bullet_1.pos)]

        self.bullet_2 = Particle(init_pos=copy.copy(b_pos), init_vel=copy.copy(b_vel))
        self.b2_path = [copy.copy(self.bullet_2.pos)]

        self.bullet_3 = Particle(init_pos=copy.copy(b_pos), init_vel=copy.copy(b_vel))
        self.b3_path = [copy.copy(self.bullet_3.pos)]



    def show(self):
        background(255)

        dt = 0.1

        gravity = np.array([0, 10])

        # Only gravity
        self.bullet_1.apply_force(gravity)
        self.bullet_1.update(dt)
        self.b1_path.append(copy.copy(self.bullet_1.pos))

        # Air resistance
        density = 1e-3
        v_sqrd = np.linalg.norm(self.bullet_2.vel)**2
        A = self.bullet_2.mass**2 # Scale area to mass
        Cd = 1
        dir = -self.bullet_2.vel/(np.linalg.norm(self.bullet_2.vel) + 1)
        air_resistance = 0.5 * density * v_sqrd * Cd * A * dir
        self.bullet_2.apply_force(gravity)
        self.bullet_2.apply_force(air_resistance)
        self.bullet_2.update(dt)
        self.b2_path.append(copy.copy(self.bullet_2.pos))

        # Wind directions
        wind_field = np.array([np.sin(self.bullet_3.pos[0]*0.1)*100, np.cos(self.bullet_3.pos[1]*0.1)*100])
        density = 1e-3
        wind_v_sqrd = np.linalg.norm(self.bullet_3.vel - wind_field)**2
        v_sqrd = np.linalg.norm(self.bullet_3.vel)**2
        A = self.bullet_3.mass**2 # Scale area to mass
        Cd = 1
        wind_dir = -(self.bullet_3.vel - wind_field)/(np.linalg.norm(self.bullet_3.vel - wind_field) + 1)
        wind_resistance = 0.5 * density * v_sqrd * Cd * A * wind_dir
        dir = -self.bullet_3.vel/(np.linalg.norm(self.bullet_3.vel) + 1)
        air_resistance = 0.5 * density * v_sqrd * Cd * A * dir

        self.bullet_3.apply_force(gravity)
        self.bullet_3.apply_force(wind_resistance)
        self.bullet_3.apply_force(air_resistance)
        self.bullet_3.update(dt)
        self.b3_path.append(copy.copy(self.bullet_3.pos))


        push()
        
        # draw bullet 1
        fill(self.pal["highlight-area"])
        stroke(self.pal["highlight-line"])
        stroke_weight(5)
        circle(self.bullet_1.pos[0], self.bullet_1.pos[1], 10)
        stroke_weight(2)
        for l in range(len(self.b1_path) - 1):
            line(self.b1_path[l][0], self.b1_path[l][1], self.b1_path[l+1][0], self.b1_path[l+1][1])

        # draw bullet 2
        fill(self.pal["basic-area"])
        stroke(self.pal["basic-line"])
        stroke_weight(5)
        circle(self.bullet_2.pos[0], self.bullet_2.pos[1], 10)
        stroke_weight(2)
        for l in range(len(self.b2_path) - 1):
            line(self.b2_path[l][0], self.b2_path[l][1], self.b2_path[l+1][0], self.b2_path[l+1][1])


        # draw bullet 3
        fill(self.pal["dark-area"])
        stroke(self.pal["dark-line"])
        stroke_weight(5)
        circle(self.bullet_3.pos[0], self.bullet_3.pos[1], 10)
        stroke_weight(2)
        for l in range(len(self.b3_path) - 1):
            line(self.b3_path[l][0], self.b3_path[l][1], self.b3_path[l+1][0], self.b3_path[l+1][1])


        pop()


