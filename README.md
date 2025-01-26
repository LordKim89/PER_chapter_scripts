To install (windows):

python -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt

To install (linux):

python -m venv venv

source venv\bin\activate

pip install -r requirements.txt

run with:

python gen_animations.py

## Animations for PER chapter
This code is used to generate animations for a Physics Education Research book on using computations in physics education.

It is possible to define your own color palette that should be used for the animations by adding a palette to the colors.py file.
The palettes name should be added as an argument to the animation.

For example:
AnimCircle(width, height, palette="new_palette")

The height and width of the animations can be adjusted. However, most of them assumes a square input and the animations have been designed
with a square input in mind.

Code written by Kim Svensson
