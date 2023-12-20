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
            converter = IcoTransmuting(filename, output_path)
            converter.convert()
        elif format == 'GIF':
            converter = GifTransmuting(filename, output_path)
            converter.convert()
        elif format == 'JPEG':
            converter = JpegTransmuting(filename, output_path)
            converter.convert()
        elif format == 'PNG':
            converter = PngTransmuting(filename, output_path)
            converter.convert()
        else:
            raise ValueError('Invalid format')


if __name__ == '__main__':
    transmuting(folder_path='./image/',
                output_path='./test', format='PNG')
