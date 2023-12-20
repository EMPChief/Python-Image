from PIL import Image


class Basic:
    def __init__(self, image_path, image_output_path):
        self.image_path = image_path
        self.image_output_path = image_output_path

    def _convert_image(self, image_path, output_path, output_format):
        image = Image.open(image_path)
        image.save(output_path, output_format)
