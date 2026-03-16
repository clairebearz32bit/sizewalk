from sizewalk import find_files

if __name__ == '__main__':
    # search_path = r"C:\Users\Claire\PycharmProjects\sizewalk"
    search_path = r"C:\Users\Claire\Documents"

    files = find_files(search_path)
    print(files)