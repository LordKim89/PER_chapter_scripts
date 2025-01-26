from p5 import *
from .colors import ColorPicker
import time
import numpy as np


# 60 frames = 1 full animation

class AnimCircle:

    def __init__(self, width_s, height_s, frames=60, save_frame=30, palette="GrayRedGreen"):
        self.frames = frames
        self.save_frame = save_frame
        self.r1 = width_s * 0.5 * 0.6
        self.r2 = height_s * 0.5 * 0.9
        self.mid_p = (width_s*0.5, height_s*0.5)
        cp = ColorPicker()
        self.pal = cp.get_palette(palette)
        self.time = 0

    
    def show(self):
        background(255)
        # big circle
        push()
        translate(self.mid_p[0], self.mid_p[1])
        stroke_weight(10)
        stroke(self.pal['light-line'])
        fill(255)
        r2 = (self.r1 + (np.cos(self.time*2*np.pi)**2)*(self.r2-self.r1))
        circle(0, 0, r2 * 2)

        # small circle
        stroke_weight(10)
        stroke(self.pal['dark-line'])
        fill(self.pal['light-area'])
        circle(0, 0, self.r1*2)

        # mid point
        stroke_weight(10)
        stroke(self.pal['highlight-line'])
        fill(self.pal['highlight-line'])
        push()
        stroke_weight(1)
        scale(20)
        point(0,0)
        pop()

        # radius 1
        stroke_weight(8)
        stroke(self.pal['highlight-line'])
        line(0,0, self.r1*np.cos(0.2), self.r1*np.sin(0.2))
        push()
        stroke_weight(1)
        translate(self.r1*np.cos(0.2), self.r1*np.sin(0.2))
        scale(20)
        point(0,0)
        pop()

        # radius 2
        stroke_weight(8)
        stroke(self.pal['highlight-line'])
        line(0,0, r2 * np.cos(-0.2), r2 * np.sin(-0.2))
        push()
        stroke_weight(1)
        translate(r2 * np.cos(-0.2), r2 * np.sin(-0.2))
        scale(20)
        point(0,0)
        pop()

        # radius text 1
        push()
        rotate(0.2)
        #text_font()
        #text_size(20)
        #text("r = 1", self.r1/2, 0)
        pop()

        pop()

        self.time += 1/60


