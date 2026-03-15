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


"""Get all the files & dirs in path above a size threshold"""
def search_dir(path, threshold):
    all_files = list()

    for _, dirs, files in os.walk(path):
        dirs[:] = [i for i in dirs if not i.startswith(".")]

        # is there a way we could optimize this? it's O(2n) rn but is kinda long
        # maybe i could concat the lists and then it'd just be 1 loop? it's O(2n) either way
        for file in files + dirs:
            file_path = os.path.join(_, file)
            file = Path(file_path)
            size = file.stat().st_size

            if size < threshold:
                continue

            file = File(size, file.name, file_path)

            if file not in all_files:
                all_files.append(File(size, file.name, file_path))

        # for d in dirs:
        #     d_path = os.path.join(_, d)
        #     d = Path(d_path)
        #     size = d.stat().st_size
        #
        #     if size < threshold:
        #         break
        #
        #     d = File(size, d.name, d_path)
        #
        #     if d not in all_files:
        #         all_files.append(File(size, d.name, d_path, is_dir=True))

    # # concat the dirs and files lists
    # all_files = dirs + files
    # print(all_files)
    # # replace all file strings with Path objects
    # all_files[:] = [Path(os.path.abspath(os.path.join(path, file))) for file in all_files]
    # # remove hidden dirs and files with sizes below threshold
    # all_files[:] = [file for file in all_files if not file.name.startswith(".")]
    # all_files[:] = [file for file in all_files if file.stat().st_size >= threshold]
    # # replace all Path objects with File objects
    # all_files[:] = [File(file.stat().st_size, file.name, file.resolve()) for file in all_files]
    #
    # # return sorted list of all files with the largest files first
    return sorted(all_files, key=lambda n: n.size, reverse=True)

if __name__ == '__main__':
    # min. size threshold for files to be included, 10mb by default
    thresh_mb = 10e6
    # thresh_mb = 0
    thresh_mib = pow(2, 20)

    search_path = r"C:\Users\Claire\Documents"

    dirs = search_dir(search_path, thresh_mb)
    print(dirs)
