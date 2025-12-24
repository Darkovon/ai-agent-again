import os

from google.genai import types


def write_file(working_directory, file_path, content):
    path_to_working = os.path.abspath(working_directory)
    # print(path_to_working)
    path_to_file = os.path.normpath(os.path.join(path_to_working, file_path))
    # print(path_to_file)

    if not  os.path.commonpath([path_to_working, path_to_file]) == path_to_working:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    os.makedirs(path_to_working, exist_ok=True)

    try:
        with open(path_to_file, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error in writing file contents: {e}"


schema_write_files = types.FunctionDeclaration(
    name="write_files",
    description="Write a file in a specified directory relative to the working directory based on content that is specfied.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file that will be written, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The string that will be written into the file after it has been created and opened."
            ),
        },
        required=["file_path"]
    ),
)
