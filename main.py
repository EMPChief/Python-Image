from Transforming import IcoTransmuting, GifTransmuting, JpegTransmuting, PngTransmuting
import os


def transmuting(folder_path, output_path, format):
    filenames = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            filenames.append(file_path)

    for filename in filenames:
        if format == 'ICO':
            converter = IcoTransmuting(
                filename, os.path.join(output_path, format))
            converter.convert()
        elif format == 'GIF':
            converter = GifTransmuting(
                filename, os.path.join(output_path, format))
            converter.convert()
        elif format == 'JPEG':
            converter = JpegTransmuting(
                filename, os.path.join(output_path, format))
            converter.convert()
        elif format == 'PNG':
            converter = PngTransmuting(
                filename, os.path.join(output_path, format))
            converter.convert()
        else:
            raise ValueError('Invalid format')


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(script_dir, 'image')
    output_dir = os.path.join(script_dir, 'completed')
    transmuting(folder_path=image_dir, output_path=output_dir, format='PNG')
