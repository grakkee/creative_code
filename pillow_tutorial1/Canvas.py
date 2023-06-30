# Class for setting up image canvas
from PIL import Image, ImageDraw

class Canvas:
    def __init__(self, run_id):
        self.run_id = run_id
        self.image = Image.new('RGB', (400, 400), "white")
        self.width, self.height = self.image.size

        self.draw_image = ImageDraw.Draw(self.image)
    
    def saveImage(self):
        self.image.save(f'output/{self.run_id}.png')