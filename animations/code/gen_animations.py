from circle_anim import AnimCircle
from contrast_anim import AnimContrast
from separate_anim import AnimSeparate
from p5 import *
import os
import sys



animator = None
animations = []
animation_index = 0
WIDTH_start = 400
HEIGHT_start = 400


frame_nr = 0

def setup():
    size(WIDTH_start, HEIGHT_start)
    setup_recordings()
    set_animation(animations[animation_index])

def draw():
    global frame_nr
    if animator == None:
        circle(np.random.random() * WIDTH_start, np.random.random() * HEIGHT_start, 10 + np.random.random()*100)
    else:
        animator.show()
        str_name = f"frames/{frame_nr:03}.png"
        p5.renderer.save_canvas(str_name, p5.renderer)
    frame_nr += 1
    if frame_nr >= 60:
        gen_gif(animations[animation_index])
        reset_setup()

def reset_setup():
    global frame_nr, animation_index
    frame_nr = 0
    setup_recordings()
    animation_index += 1
    if animation_index >= len(animations):
        print("NO MORE ANIMATIONS TO GENERATE")
        exit()
    set_animation(animations[animation_index])

def gen_gif(name):
    os.system("echo Generating gif")
    gif_command = "echo y | ffmpeg -framerate 24 -i frames\%03d.png -filter_complex  \"[0]split[a][b]; [a]palettegen[palette]; [b][palette]paletteuse\" " + name + ".gif"
    os.system(gif_command)
    os.system("echo Y | copy frames\\024.png "+name+"_stationary.png")

def setup_recordings():
    if os.path.isdir("frames"):
        os.system("rm -r frames")
    os.system("mkdir frames")




def set_animation(anim_name):
    global animator
    if anim_name == None:
        animator = None

    if anim_name == "VLT_circle":
        animator = AnimCircle(WIDTH_start, HEIGHT_start)

    if anim_name == "VLT_contrast":
        animator = AnimContrast(WIDTH_start, HEIGHT_start)

    if anim_name == "VLT_separate":
        animator = AnimSeparate(WIDTH_start, HEIGHT_start)


if __name__ == "__main__":
    #animations = ["VLT_circle", "VLT_contrast", "VLT_separate"]
    animations = ["VLT_separate"]
    obj = run(renderer="skia")

