from sizewalk import find_files, b_to_any
import time

if __name__ == '__main__':
    search_path = r"."
    # search_path = r"C:\Users\Claire"

    thresh = 0
    # thresh = 10e6

    start = time.time()
    files = find_files(search_path, threshold=thresh)
    dirs = [d for d in files if d.is_dir]

    num_dirs = len(dirs)
    num_files = len(files) - num_dirs

    size_files = sum([f.size for f in files])
    size_files, size_suffix = b_to_any(size_files)

    elapsed = time.time() - start

    print(files)
    print(f"{num_files} files totaling {size_files:.2f} {size_suffix} found and {num_dirs} directories found after {elapsed:.1f} seconds.")