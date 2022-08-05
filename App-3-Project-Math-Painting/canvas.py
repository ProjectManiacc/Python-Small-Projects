import numpy as np
from PIL import Image
from numpy import uint8


class Canvas:
    def __init__(self, height=1, width=1, color=[0, 0, 0]):
        self.height = height
        self.width = width
        self.color = color

    def create_matrix(self):
        self.data = np.zeros((self.height, self.width, 3),dtype=uint8)
        self.data[:] = self.color

    def make(self, imagepath):
        print(self.data,self.color)
        img = Image.fromarray(self.data, "RGB")
        img.save(imagepath)
