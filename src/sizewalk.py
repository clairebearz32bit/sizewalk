import os
from pathlib import Path


class File:
    def __init__(self, size, name, full_path, is_dir=False):
        self.full_path = full_path
        self.name = name
        self.size = size
        self.is_dir = is_dir

        # self.size is in bytes,
        self.sizeMB = self.size / 1e6

    def __repr__(self):
        if self.is_dir:
            return f"{self.name}/: {self.sizeMB}MB"
        return f"{self.name}: {self.sizeMB:.1f}MB"


def find_files(path, threshold=10e6):
    """finds and returns a list with all the files in a directory, sorted by the largest files first

    :parameter path: the full path to the directory
    :parameter threshold: minimum size in bytes of files to return
    """
    print(os.path.abspath(path))
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path '{path}' could not be found.")

    all_files = list()

    for _, dirs, files in os.walk(path):
        # remove all hidden dirs
        dirs[:] = [i for i in dirs if not i.startswith(".")]

        for file in files + dirs:
            file_path = os.path.join(_, file)
            file = Path(file_path)
            stat = file.stat()

            size = stat.st_size
            is_dir = file.is_dir()

            if size < threshold:
                continue

            file = File(size, file.name, file_path)

            if file not in all_files:
                all_files.append(File(size, file.name, file_path, is_dir=is_dir))

    # return sorted list of all files with the largest files first
    return sorted(all_files, key=lambda n: n.size, reverse=True)
