from circle_anim import AnimCircle
from contrast_anim import AnimContrast
from separate_anim import AnimSeparate
from earth_anim import AnimEarth
from hunter_anim import AnimHunter
from ballistic_anim import AnimBallistic
from wave_anim import AnimWave
from pendulum_anim import AnimPendulum
from heat_anim import AnimHeat
from cloth_anim import AnimCloth
from solid_anim import AnimSolid
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
    if frame_nr >= animator.frames:
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
    mp4_command = "echo y | ffmpeg -framerate 24 -i frames\%03d.png -filter_complex  \"[0]split[a][b]; [a]palettegen[palette]; [b][palette]paletteuse\" " + name + ".mp4"
    os.system(mp4_command)
    gif_command = "echo y | ffmpeg -framerate 24 -i frames\%03d.png -filter_complex  \"[0]split[a][b]; [a]palettegen[palette]; [b][palette]paletteuse\" " + name + ".gif"
    os.system(gif_command)
    frame_str = f"frames\\{animator.save_frame:03d}.png"
    print("echo Y | copy " + frame_str + " "+name+"_stationary.png")
    os.system("echo Y | copy " + frame_str + " "+name+"_stationary.png")

def setup_recordings():
    if os.path.isdir("frames"):
        os.system("rmdir frames /S /Q")
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

    if anim_name == "PRJ_earth":
        animator = AnimEarth(WIDTH_start, HEIGHT_start)

    if anim_name == "PRJ_hunter":
        animator = AnimHunter(WIDTH_start, HEIGHT_start)

    if anim_name == "PRJ_ballistic":
        animator = AnimBallistic(WIDTH_start, HEIGHT_start)

    if anim_name == "PRJ_wave":
        animator = AnimWave(WIDTH_start, HEIGHT_start)

    if anim_name == "PRJ_pendulum":
        animator = AnimPendulum(WIDTH_start, HEIGHT_start)

    if anim_name == "PRJ_heat":
        animator = AnimHeat(WIDTH_start, HEIGHT_start)

    if anim_name == "PRJ_cloth":
        animator = AnimCloth(WIDTH_start, HEIGHT_start)

    if anim_name == "PRJ_solid":
        animator = AnimSolid(WIDTH_start, HEIGHT_start)



if __name__ == "__main__":
    #"""
    animations = ["VLT_circle", 
                "VLT_contrast", 
                "VLT_separate", 
                "PRJ_earth", 
                "PRJ_hunter", 
                "PRJ_ballistic", 
                "PRJ_wave", 
                "PRJ_pendulum", 
                "PRJ_heat",
                "PRJ_cloth",
                "PRJ_solid"]
    #"""
    animations = ["PRJ_earth"]
    obj = run(renderer="skia")

