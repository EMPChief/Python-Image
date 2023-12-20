# main.py
from transmuting import IcoTransmuting, GifTransmuting, JpegTransmuting, PngTransmuting


def transmuting(filenames, output_path, format):
    for filename in filenames:
        if format == 'ICO':
            converter = IcoTransmuting(filename, output_path)
            converter.convert_to_ico()
        elif format == 'GIF':
            converter = GifTransmuting(filename, output_path)
            converter.convert_to_gif()
        elif format == 'JPEG':
            converter = JpegTransmuting(filename, output_path)
            converter.convert_to_jpeg()
        elif format == 'PNG':
            converter = PngTransmuting(filename, output_path)
            converter.convert_to_png()
        else:
            raise ValueError('Invalid format')


if __name__ == '__main__':
    transmuting(filenames=['./python-image/IMG_4360.JPG'],
                output_path='./test', format='PNG')
