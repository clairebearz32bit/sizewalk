import argparse

from src.sizewalk import find_files


def parse():
    parser = argparse.ArgumentParser()
    parser.parse_args()


if __name__ == '__main__':
    parse()

Create new files, move all code to src folder, and refactor main.py

Create cli.py and sizewalk.py, and move all contents of main.py to sizewalk.py. Update README.md and create LICENSE.md

cli.py, main.py
Created cli.py
Created sizewalk.py
Moved all code from main.py to sizewalk.py
Updated README
Created LICENSE.md
Created src dir and moved all code files into it