import numpy as np
from p5 import *
from particle import Particle
from colors import ColorPicker
import copy

class AnimEarth:

    

    def __init__(self, wi, he, frames=366, save_frame=250):
        self.frames = frames
        self.save_frame = save_frame
        self.w = wi
        self.h = he
        cp = ColorPicker()
        self.pal = cp.get_palette("GrayRedGreen")

        self.sun = Particle(mass=1.989e30)
        self.earth = Particle(init_pos=np.array([150e9, 0], dtype=np.float64), init_vel=np.array([0, 29784.8], dtype=np.float64), mass=5.9721e24)
        moon_vel = np.array([0, 2 * np.pi * 384.4e6 / (28 * 60*60*24)], dtype=np.float64) + self.earth.vel
        self.moon = Particle(init_pos=self.earth.pos+np.array([384.4e6, 0], dtype=np.float64), init_vel=moon_vel, mass=7.34767309e22)

        self.scale_factor = np.linalg.norm(self.moon.pos)*1.1 /(self.w * 0.5)

        self.earth_path = [copy.copy(self.earth.pos/self.scale_factor)]
        self.moon_path = [copy.copy((self.moon.pos - self.earth.pos)*30/self.scale_factor)]

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


        self.interact(self.sun, self.earth)
        self.interact(self.sun, self.moon)
        self.interact(self.earth, self.moon)

        self.earth.update(60*60*24)
        self.moon.update(60*60*24)

        self.earth_path.append(copy.copy(self.earth.pos/self.scale_factor))
        self.moon_path.append(copy.copy((self.moon.pos - self.earth.pos)*30/self.scale_factor))



        push()
        stroke_weight(2)
        stroke(self.pal["highlight-line"])
        translate(self.w*0.5, self.h*0.5)
        for i in range(len(self.earth_path) - 1):
            push()
            translate(self.earth_path[i][0], self.earth_path[i][1])
            circle(self.moon_path[i][0], self.moon_path[i][1], 2)
            pop()
            #line(self.moon_path[i][0], self.moon_path[i][1], self.moon_path[i+1][0], self.moon_path[i+1][1])

        pop()


        push()

        translate(self.w*0.5,self.h*0.5)
        no_stroke()
        fill(200, 200, 40)
        circle(0, 0, 40)

        translate(self.earth.pos[0]/self.scale_factor, self.earth.pos[1]/self.scale_factor)
        fill(70, 90, 230)
        circle(0, 0, 20)
        
        mp = (self.moon.pos - self.earth.pos)/self.scale_factor
        translate(mp[0]* 30, mp[1] * 30 )
        fill(120, 120, 120)
        circle(0, 0, 10)

        pop()



        
        
