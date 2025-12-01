import os

working_directory = "ai_agent_again/"

def get_files_info(working_directory, directory="."):

    path_to_working = os.path.abspath(working_directory)
    full_path = os.path.join(path_to_working, directory)

    if not full_path.startswith(path_to_working):
        return (f'Error: Cannot list {directory} as it is outside the permitted working directory"')
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        file_list = os.listdir(full_path)
        contents = []
        for file in file_list:
            file_path = os.path.join(full_path, file)
            contents.append(f"- {file}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}")

        files = "\n".join(contents)

        return files
    except Exception as e:
        return f"Error listing files: {e}"

    #abs_path_to_dir = os.path.join(path_to_working, directory)
    #if abs_path_to_dir !=

get_files_info("calculator")
