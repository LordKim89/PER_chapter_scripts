from p5 import *
from colors import ColorPicker
import time
import numpy as np


# 60 frames = 1 full animation

class AnimSeparate:

    def __init__(self, width_s, height_s, frames=60, save_frame=0):
        self.frames = frames
        self.save_frame = save_frame

        self.mid_p = (width_s*0.5, height_s*0.5)
        cp = ColorPicker()
        self.pal = cp.get_palette("GrayRedGreen")
        self.time = 0

    



    def show(self):
        background(255)
        translate(self.mid_p[0], self.mid_p[1])
        push()

        lerp_factor = lerp(0, 1, np.sin(self.time*np.pi)**2)

        r1_area = 255 * (lerp_factor * self.pal["highlight-area"]._red + (1 - lerp_factor) * self.pal["basic-area"]._red)
        g1_area = 255 * (lerp_factor * self.pal["highlight-area"]._green + (1 - lerp_factor) * self.pal["basic-area"]._green)
        b1_area = 255 * (lerp_factor * self.pal["highlight-area"]._blue + (1 - lerp_factor) * self.pal["basic-area"]._blue)

        r1_line = 255 * (lerp_factor * self.pal["highlight-line"]._red + (1 - lerp_factor) * self.pal["basic-line"]._red)
        g1_line = 255 * (lerp_factor * self.pal["highlight-line"]._green + (1 - lerp_factor) * self.pal["basic-line"]._green)
        b1_line = 255 * (lerp_factor * self.pal["highlight-line"]._blue + (1 - lerp_factor) * self.pal["basic-line"]._blue)


        r2_area = 255 * ((1 - lerp_factor) * self.pal["highlight-area"]._red + (lerp_factor) * self.pal["basic-area"]._red)
        g2_area = 255 * ((1 - lerp_factor) * self.pal["highlight-area"]._green + (lerp_factor) * self.pal["basic-area"]._green)
        b2_area = 255 * ((1 - lerp_factor) * self.pal["highlight-area"]._blue + (lerp_factor) * self.pal["basic-area"]._blue)

        r2_line = 255 * ((1 - lerp_factor) * self.pal["highlight-line"]._red + (lerp_factor) * self.pal["basic-line"]._red)
        g2_line = 255 * ((1 - lerp_factor) * self.pal["highlight-line"]._green + (lerp_factor) * self.pal["basic-line"]._green)
        b2_line = 255 * ((1 - lerp_factor) * self.pal["highlight-line"]._blue + (lerp_factor) * self.pal["basic-line"]._blue)


        push()
        translate(-self.mid_p[0]*0.5, 0)
        fill(r1_area, g1_area, b1_area)
        stroke(r1_line, g1_line, b1_line)
        stroke_weight(10)
        circle(0, 0, self.mid_p[0]*0.8, mode=CENTER)
        pop()

        push()
        translate(self.mid_p[0]*0.5, 0)
        fill(r2_area, g2_area, b2_area)
        stroke(r2_line, g2_line, b2_line)
        stroke_weight(10)
        circle(0, 0, self.mid_p[0]*0.8, mode=CENTER)
        pop()


       
        pop()


        self.time += 1/60


