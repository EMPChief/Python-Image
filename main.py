from Utils import Converter, Utils
import os


def transmuting(folder_path, output_path, format):
    filenames = Utils.get_filenames(folder_path)

    for filename in filenames:
        converter = Converter(filename, output_path)
        converter.convert(format)


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(script_dir, 'image')
    output_dir = os.path.join(script_dir, 'completed')
    transmuting(folder_path=image_dir, output_path=output_dir, format='PNG')
