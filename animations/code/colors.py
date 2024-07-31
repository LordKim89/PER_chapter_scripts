from p5 import *

class ColorPicker:
    def __init__(self):
        self._setup_palettes()

    def _setup_palettes(self):
        self.palettes = dict()

        # A palette should have the follow colors:
        #   dark-line - used for lines and dots and text
        #   light-line - used for for faded lines and dots
        #   dark-area - used for dark areas
        #   light-area - used for light areas
        #   highlight-line - used for highlighting something strongly
        #   highlight-area - used for highlighting something weakly
        #   basic-line - used for basic colors
        #   basic-area - used for basic area
        
        # Gray Red Green palette
        gro = dict()
        gro['dark-line'] = Color(50, 50, 50)
        gro['light-line'] = Color(150, 150, 150)
        gro['dark-area'] = Color(180, 180, 180)
        gro['light-area'] = Color(220, 220, 220)
        gro['highlight-line'] = Color(220, 50, 50)
        gro['highlight-area'] = Color(240, 75, 75)
        gro['basic-line'] = Color(75, 200, 75)
        gro['basic-area'] = Color(100, 220, 100)


        self.palettes['GrayRedGreen'] = gro

    def get_palette(self, st):
        if st in self.palettes.keys():
            return self.palettes[st]
        raise ValueError
