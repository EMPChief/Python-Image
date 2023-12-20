from .basic import Basic
from PIL import Image


# PngTransmuting.py
from .basic import Basic
from PIL import Image


class PngTransmuting(Basic):
    def __init__(self, image_path, image_output_path):
        super().__init__(image_path, image_output_path)

    def convert_to_png(self):
        self._convert_image(self.image_path, self.image_output_path, 'PNG')
