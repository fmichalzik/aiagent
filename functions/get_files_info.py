import os
import pathlib

def get_files_info(working_directory, directory=None):

    dir = pathlib.PurePath(directory)

    # check if the directory argument is outside the working_directory
    if not dir.is_relative_to(working_directory): # PurePath().is_relative() checks whether the path belongs to the other given path or not
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # check if 'directory' actually is a directory
    try:
        if not os.path.isdir(dir): 
            return f'Error: "{directory}" is not a directory'
    except Exception as e:
        return f"Error encountered: {e}"
   
    # helper function to print file infos
    def file_info_to_string(name, size, is_dir):
        return f"- {name}: file_size={size} bytes, is_dir={is_dir}"
    
    try: 
        file_infos = [] # collects file_info for each content in directory
        # lists the content in directory
        directory_cotents = os.listdir(dir)
        # iterating over content to collect file info
        for content in directory_cotents:
            path = dir.joinpath(content)
            if os.path.isfile(path):
                file_infos.append(file_info_to_string(content, os.path.getsize(path), False))
            if os.path.isdir(path):
                file_infos.append(file_info_to_string(content, os.path.getsize(path), True))

        # join file_infos to one string with linebreaks
        info_string = '\n'.join(file_infos)
        # return info_string
        return info_string
    except Exception as e:
        return f"Error listing files: {e}"