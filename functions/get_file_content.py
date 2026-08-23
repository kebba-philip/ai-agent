import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:

    try:

        abs_working_dir = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if not abs_file_path.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'


        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        content = ""
        with open(file_path, "r") as file:
            file_content = file.read(MAX_CHARS)

            if len(file_content) >= MAX_CHARS

        return content

    except Exception as e:
        return f"Error: {e}"
