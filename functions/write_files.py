import os


def write_file(working_directory, file_path, content):
    path_to_working = os.path.abspath(working_directory)
    print(path_to_working)
    path_to_file = os.path.normpath(os.path.join(path_to_working, file_path))
    print(path_to_file)

    if not os.path.commonpath([path_to_working, path_to_file]) == path_to_working:
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
