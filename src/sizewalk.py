import os
from pathlib import Path

from math import log2, floor


def b_to_any(n: int):
    suffixes = {10: "KB", 20: "MB", 30: "GB", 40: "TB"}
    power = 10 * floor(log2(n) / 10)
    size = (n / pow(2, power))

    return size, suffixes[power]

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
        suffixes = {10: "KB", 20: "MB", 30: "GB", 40: "TB"}
        prefix = "FILE" if not self.is_dir else "DIR"
        power = 10 * floor(log2(self.size) / 10)
        size = (self.size / pow(2, power))

        return f"{prefix} {self.name} {power} : {size:.1f} {suffixes[power]}"


def find_files(path, threshold=10e6):
    """finds and returns a list with all the files in a directory, sorted by the largest files first

    :parameter path: the full path to the directory
    :parameter threshold: minimum size in bytes of files to return
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path '{path}' could not be found.")

    # all_files = list()
    all_files = set()

    for root, dirs, files in os.walk(path):
        # remove all hidden dirs
        dirs[:] = [i for i in dirs if not i.startswith(".")]

        files += dirs
        files = set(files)

        for file in files:
            try:
                file_path = os.path.join(root, file)
                file = Path(file_path)
                stat = file.stat()

                size = stat.st_size

                if size < threshold:
                    continue

                file = File(size, file.name, file_path, is_dir=file.is_dir())
                all_files.add(file)

            except FileNotFoundError as fnfe:
                print(f"File: {file} not found.")
                continue

    # return sorted list of all files with the largest files first
    return sorted(all_files, key=lambda n: n.size, reverse=True)
