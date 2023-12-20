# basic.py
from PIL import Image
import os


class Basic:
    def __init__(self, image_path, image_output_path):
        self.image_path = image_path
        self.image_output_path = image_output_path

    def _convert_image(self, output_format):
        image = Image.open(self.image_path)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, self.image_output_path)
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, f"output.{
                                   output_format.lower()}")
        image.save(output_file, output_format)
