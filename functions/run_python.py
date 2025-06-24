import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'

    if os.path.splitext(file_path)[-1] != ".py":
        return f'Error: "{file_path}" is not a Python file.'

    try:
        process = subprocess.run(['chmod', '+x', abs_file_path], capture_output=True, text=True, timeout=30)
        output = [f"STDOUT: {process.stdout}", f"STDERR: {process.stderr}"]

        if process.returncode != 0:
            output.append("Process exited with code X")
        
        if process.stdout == None:
            output.append("No output produced.")
        
        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
