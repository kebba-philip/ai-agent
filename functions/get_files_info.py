import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)

        target_dir = os.path.normpath(
            os.path.join(abs_working_dir, directory)
        )

        if os.path.commonpath(
            [abs_working_dir, target_dir]
        ) != abs_working_dir:
            return (
                f'Error: Cannot list "{directory}" '
                "as it is outside the permitted working directory"
            )

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        final_response = ""
        contents = os.listdir(target_dir)

        for content in contents:
            content_path = os.path.join(target_dir, content)
            is_dir = os.path.isdir(content_path)
            size = os.path.getsize(content_path)

            final_response += (
                f"- {content}: file_size={size} bytes, "
                f"is_dir={is_dir}\n"
            )

        return final_response

    except Exception as e:
        return f"Error: {e}"
