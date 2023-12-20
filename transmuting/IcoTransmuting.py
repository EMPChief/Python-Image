from .basic import Basic
from PIL import Image


class IcoTransmuting(Basic):
    def __init__(self, image_path, image_output_path):
        super().__init__(image_path, image_output_path)

    def convert_to_ico(self):
        self._convert_image(self.image_path, self.output_path, 'ICO')
