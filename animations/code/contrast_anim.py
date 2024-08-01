from p5 import *
from colors import ColorPicker
import time
import numpy as np


# 60 frames = 1 full animation

class AnimContrast:

    def __init__(self, width_s, height_s, frames=60):
        self.frames = frames

        self.mid_p = (width_s*0.5, height_s*0.5)
        cp = ColorPicker()
        self.pal = cp.get_palette("GrayRedGreen")
        self.time = 0

    
    def draw_spiral(self, freq):
        stroke_weight(10)
        stroke(self.pal["dark-line"])
        for k in range(100):
            line(50*np.sin(freq*k + self.time*2*np.pi*freq*10), k*3,   50*np.sin(freq*(k+1) +  self.time*2*np.pi*freq*10), 3 * (k+1))





    def show(self):
        background(255)
        push()

        translate(self.mid_p[0], self.mid_p[1])
        
        push()
        translate(-self.mid_p[0] * 0.5, -self.mid_p[1] * 0.75)
        self.draw_spiral(0.1)
        pop()

        push()
        translate(self.mid_p[0] * 0.5, -self.mid_p[1] * 0.75)
        self.draw_spiral(0.3)
        pop()



        # right spiral

        pop()


        self.time += 1/60


