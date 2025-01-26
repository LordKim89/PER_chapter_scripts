import numpy as np
from p5 import *
from .particle import Particle
from .colors import ColorPicker
import copy

class AnimSolid:
    def __init__(self, wi, he, frames=200, palette="GrayRedGreen"):
        self.frames = frames
        self.save_frame = 150
        self.w = wi
        self.h = he
        self.time = 0
        cp = ColorPicker()
        self.pal = cp.get_palette(palette)
        
        self.dl = self.w * 0.8/(40 - 1)

        self.particles = []

        for n in range(7):
            for m in range(35):
                pos = np.array([n * self.dl + self.w*0.7, m * self.dl + self.h*0.25])
                self.particles.append(Particle(init_pos=pos))
                self.particles[-1].oldForce = None
                self.particles[-1].neighbours = []
                self.particles[-1].n_length = []
                self.particles[-1].fixed = False
                if m == 34:
                    self.particles[-1].fixed = True

        for n in range(30):
            for m in range(5):
                pos = np.array([-(n+1) * self.dl + self.w * 0.7, m * self.dl + self.h * 0.25])
                self.particles.append(Particle(init_pos=pos))
                self.particles[-1].oldForce = 1
                self.particles[-1].neighbours = []
                self.particles[-1].n_length = []
                self.particles[-1].fixed = False

        for rows in range(10):
            pos = np.array([-10*self.dl + self.w * 0.7 + rows * self.dl, (rows+5)*self.dl + self.h * 0.25 ])
            self.particles.append(Particle(init_pos=pos))
            self.particles[-1].oldForce = 1
            self.particles[-1].neighbours = []
            self.particles[-1].n_length = []
            self.particles[-1].fixed = False
            if rows > 0:
                pos = np.array([-10*self.dl + self.w * 0.7 + (rows) * self.dl, (rows+4)*self.dl + self.h * 0.25 ])
                self.particles.append(Particle(init_pos=pos))
                self.particles[-1].oldForce = 1
                self.particles[-1].neighbours = []
                self.particles[-1].n_length = []
                self.particles[-1].fixed = False


        for p in self.particles:
            for o in self.particles:
                dl = np.linalg.norm(p.pos - o.pos)
                if dl > 0:
                    if dl < self.dl*1.5:
                        p.neighbours.append(o)
                        p.n_length.append(dl)






       



    def show(self):
        background(255)

        push()

        gravity = np.array([0, 10])
        k = 1000000
        dt = 0.00001

        for _ in range(1000):
            for p in self.particles:
                force = 0
                oldforce = 0.01
                for i, o in enumerate(p.neighbours):
                    dv = p.pos - o.pos
                    dl = np.linalg.norm(dv)
                    dir = -dv/(dl + 1)
                    force += dir * k * (dl - p.n_length[i])
                    oldforce += np.linalg.norm(force)
                p.apply_force(gravity)
                p.apply_force(force)
                p.oldForce = oldforce


            for p in self.particles:
                if not p.fixed:
                    p.update(dt)
                else:
                    p.force = np.array([0,0], dtype=np.float64)


        
                # show
        #stroke(self.pal["light-line"])
        #stroke_weight(2)
        #for p in self.particles:
        #    for o in p.neighbours:
        #        line(p.pos[0], p.pos[1], o.pos[0], o.pos[1])

        no_stroke()
        for p in self.particles:
            lf = (lerp(0, 1, np.log10(p.oldForce)/3) + 0.1)**2
            #print(lf, p.oldForce)
            cr = (200 * lf + 30)
            cg = (10) + 255*max(0, lf - 1)
            cb = (200 * (1 - lf) + 30) + 255*max(0, lf - 1)
            fill(cr, cg, cb)
            circle(p.pos[0], p.pos[1], self.dl*1.6)

        pop()


        self.time += 1/60


