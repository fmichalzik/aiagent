from pathlib import Path


def get_file_content(working_directory, file_path):

    # If the file_path is outside the working_directory, 
    # return a string with an error
    path = Path(file_path)
    if not path.is_relative_to(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # If the file_path is not a file, return an error string:
    if not path.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # Read the file and return its contents as a string
    try:
        MAX = 10000
        with path.open() as f:
            content= f.readlines(MAX)
            content_string = ''.join(content)
            if len(content_string) > MAX:
                content_string = content_string + f'[...File "{file_path}" truncated at 10000 characters]'
            return content_string
    except Exception as e:
        return f"Error reading file: {e}"
