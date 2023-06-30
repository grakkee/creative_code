# class for creating and drawing lines
from PIL import Image, ImageDraw

class Line:
    def __init__(self, pa, pb, fill=None, width=None):
        self.pa = pa
        self.pb = pb
        self.fill = fill
        self.width = width
    
    def draw(self, draw_image):
        draw_image.line([self.pa, self.pb], fill="black", width=3)