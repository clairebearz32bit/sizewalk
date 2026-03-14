import os
from pathlib import Path


class File:
    def __init__(self, size, name, full_path):
        self.full_path = full_path
        self.name = name
        self.size = size

        # self.size is in bytes,
        self.sizeGiB = self.size / 1e9

    def __repr__(self):
        return f"{self.name}: {self.size/1e6:.2f}MB"


def search_dir(path, threshold):
    listed = os.walk(path)
    _, dirs, files = next(listed)

    # concat the dirs and files lists
    all_files = dirs + files
    # replace all file strings with Path objects
    all_files[:] = [Path(os.path.abspath(os.path.join(path, file))) for file in all_files]
    # remove hidden dirs and files with sizes below threshold
    all_files[:] = [file for file in all_files if not file.name.startswith(".")]
    all_files[:] = [file for file in all_files if file.stat().st_size >= threshold]
    # replace all Path objects with File objects
    all_files[:] = [File(file.stat().st_size, file.name, file.resolve()) for file in all_files]

    # return sorted list of all files with the largest files first
    return sorted(all_files, key=lambda n: n.size, reverse=True)


if __name__ == '__main__':
    # min. size threshold for files to be included, 10mb by default
    thresh_mb = 10e6
    # thresh_mb = 0
    thresh_mib = pow(2, 20)

    search_path = r"C:\Users\Claire\Documents"

    dirs = search_dir(search_path, thresh_mb)
    print(dirs)
