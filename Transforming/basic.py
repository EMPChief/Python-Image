from PIL import Image
import os


class Basic:
    def __init__(self, image_path, image_output_path):
        self.image_path = image_path
        self.image_output_path = image_output_path

    def _get_output_file_name(self, extension):
        base_name = os.path.splitext(os.path.basename(self.image_path))[0]
        return f"{base_name}.{extension.lower()}"

    def _get_output_file_path(self, output_format):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(script_dir, self.image_output_path)
        os.makedirs(output_dir, exist_ok=True)
        return os.path.join(output_dir, self._get_output_file_name(output_format))

    def _convert_image(self, output_format):
        image = Image.open(self.image_path)
        output_file_path = self._get_output_file_path(output_format)
        image.save(output_file_path, output_format)
