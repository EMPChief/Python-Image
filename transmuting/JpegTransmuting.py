from .basic import Basic
from PIL import Image


class JpegTransmuting(Basic):
    def __init__(self, image_path, image_output_path):
        super().__init__(image_path, image_output_path)

    def convert_to_jpeg(self):
        self._convert_image(self.image_path, self.output_path, 'JPEG')
