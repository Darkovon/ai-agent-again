import os

from google.genai import types

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


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file in a specified directory relative to the working directory, providing file content",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to read from, relative to the working directory",
            ),
        },
        required=["file_path"]
    ),
)
