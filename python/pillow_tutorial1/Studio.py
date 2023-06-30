# class where all the art is generated


# ideas: basic algebraic functions, derivatives, integrals, plotted series, sequences
# functions: linear, parabola, x^n, n^x, log(x), e^x
# series/sequences: fibonnacci, lazy caterer,  etc

from PIL import Image, ImageDraw
import random
from Canvas import Canvas
from Line import Line

class Studio:
    def __init__(self, run_id):
        self.canvas = Canvas(run_id)
    
    def drawRandomLine(self):
        line = Line((100,200), (150,300))
        line.draw(self.canvas.draw_image)
    
    def save(self):
        self.canvas.saveImage()