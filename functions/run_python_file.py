import os
import subprocess
from google.genai import types

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
        process = subprocess.run(['python3', abs_file_path], capture_output=True, text=True, timeout=30,)
        output = []
        if process.stdout:
            output.append(f"STDOUT:\n{process.stdout}")
        if process.stderr:
            output.append(f"STDERR:\n{process.stderr}")

        if process.returncode != 0:
            output.append(f"Process exited with code {process.returncode}")
        
        if process.stdout == None:
            output.append("No output produced.")
        
        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"

# We can use types.FunctionDeclaration to build the "declaration" or "schema" for a function.
# This basically just tells the LLM how to use the function. 
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the py file at the specified file_path, returning data like STDOUT, STDERR.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file_path to the py file, relative to the working directory.",
            ),
        },
    ),
)
