from PIL import Image
import os
from .Utils import Utils


class Converter:
    def __init__(self, filename, output_path):
        self.filename = filename
        self.output_path = output_path

    def convert(self, output_format):
        image = Image.open(self.filename)
        output_file_path = Utils.get_output_file_path(
            self.filename, output_format, self.output_path)
        image.save(output_file_path, output_format.upper())
