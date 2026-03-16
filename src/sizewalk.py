import os
from pathlib import Path
from math import ceil, log2


class File:
    def __init__(self, size, name, full_path, is_dir=False):
        self.full_path = full_path
        self.name = name
        self.size = size
        self.is_dir = is_dir

        # self.size is in bytes,
        self.sizeMB = self.size / 1e6

    # TODO Make this less awful
    def __repr__(self):
        prefix = "FILE" if not self.is_dir else "DIR"
        SIZES = {1: "B", 2: "B", 3: "KB", 4: "KB", 5: "KB", 6: "MB", 7: "MB", 8: "MB", 9: "GB", 10: "GB", 11: "GB"}
        size = len(str(self.size))
        size = (size - (size % 3)) - 3
        suffix = SIZES[size]


        return f"{prefix} {self.name}: {self.size/(pow(10, size)):.1f} {suffix}"


def find_files(path, threshold=10e6):
    """finds and returns a list with all the files in a directory, sorted by the largest files first

    :parameter path: the full path to the directory
    :parameter threshold: minimum size in bytes of files to return
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path '{path}' could not be found.")

    all_files = list()

    for root, dirs, files in os.walk(path):
        # remove all hidden dirs
        dirs[:] = [i for i in dirs if not i.startswith(".")]

        for file in files + dirs:
            try:
                file_path = os.path.join(root, file)
                file = Path(file_path)
                stat = file.stat()

                size = stat.st_size

                if size < threshold:
                    continue

                file = File(size, file.name, file_path, is_dir=file.is_dir())

                if file not in all_files:
                    all_files.append(file)

            except FileNotFoundError as fnfe:
                continue

    # return sorted list of all files with the largest files first
    return sorted(all_files, key=lambda n: n.size, reverse=True)
