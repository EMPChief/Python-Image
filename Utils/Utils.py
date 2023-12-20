import os


class Utils:
    @staticmethod
    def get_filenames(folder_path):
        return [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file_name))]

    @staticmethod
    def get_output_file_path(filename, output_format, output_path):
        base_name = os.path.splitext(os.path.basename(filename))[0]
        return os.path.join(output_path, f"{base_name}.{output_format.lower()}")
