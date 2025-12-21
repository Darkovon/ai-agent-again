import os
import subprocess

from google.genai import types


def run_python_file(working_directory, file_path, args=None):

    # Let's make sure the file is real and in the permitted dir.

    path_to_working = os.path.abspath(working_directory)
    print(path_to_working)
    path_to_file = os.path.normpath(os.path.join(path_to_working, file_path))
    print(path_to_file)

    if not os.path.commonpath([path_to_working, path_to_file]) == path_to_working:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    file_exists = os.path.isfile(file_path)
    file_is_dir = os.path.isdir(file_path)
    file_is_py = file_path.endswith(".py")

    if not file_is_py:
        return f'Error: "{file_path}" is not a Python file'
    if not file_exists or file_is_dir:
        return f'Error: "{file_path}" does not exist or is not a regular file'


    # Pass the file in as a subprocess
    command = ["python3", path_to_file]

    if args != None:
        command.extend(args)

    # Try to run it and capture the output
    try:
        completed_process = subprocess.run(
        command,
        capture_output=True,
        cwd=path_to_working,
        timeout=30,
        text=True)

        process_stdout = completed_process.stdout
        process_stderr = completed_process.stderr
        process_return_code = completed_process.returncode

        output_string = build_output_string(process_stdout, process_stderr, process_return_code)

        return output_string

    except Exception as e:
        return f"Error: executing python file: {e}"


def build_output_string(stdout, stderr, return_code):
    outputs = []

    if stdout == "" and stderr == "":
        outputs.append("No output produced")
    if return_code != 0:
        outputs.append(f"Process exited with code {return_code}")
    if stdout:
        outputs.append(f"STDOUT: {stdout}")
    if stderr:
        outputs.append(f"STDERR: {stderr}")

    output_string = "\n".join(outputs)
    return output_string

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file in a specified directory relative to the working directory as a subprocess, provides stdout, stderr, and exit code if needed. Args can be provded that can be run with the file, but args defaults to the value None",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file that will be run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING
                ),
                description="An array of strings that are being passed with the intention to be executed with the file path. The default value is None"
            ),
        },
        required=["file_path"]
    ),
)
