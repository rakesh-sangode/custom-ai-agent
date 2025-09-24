import os


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working directory'

    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.mkdir(parent_dir)
        except Exception as err:
            return f"Could not create parent dirs: {parent_dir} = {err}"

    if not os.path.isfile(abs_file_path):
        pass
        # parent_dir = os.path.dirname(abs_file_path)
        # try:
        #     os.mkdir(parent_dir)
        # except Exception as err:
        #     return f"Could not create parent dirs: {parent_dir} = {err}"

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as err:
        return f"Failed to write to file: {file_path}, {err}"
