import os
from re import L
from sre_compile import MAXCODE

from config import MAX_CHARS


def get_file_content(working_directory, file_path):

    try:
        path_to_working = os.path.abspath(working_directory)
        print(path_to_working)
        path_to_file = os.path.normpath(os.path.join(path_to_working, file_path))
        print(path_to_file)

        if not os.path.commonpath([path_to_working, path_to_file]) == path_to_working:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        file_exists = os.path.isfile(path_to_file)
        file_is_dir = os.path.isdir(path_to_file)

        if not file_exists or file_is_dir:
            return f'Error: "{file_path}" does not exist or is not a regular file'


        with open(path_to_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string

    except Exception as e:
        return f'Error while reading file: {e}'
