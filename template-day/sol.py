"""Used as the solution for the Xth day in python"""

import time
import os

def change_dir():
    """For python debugging"""
    os.chdir("PWD HERE")

def read_file(file_path):
    """Used to read a files content and return said content"""
    read_input = ''
    with open(file_path, "r", encoding="utf-8") as file:
        read_input = file.read()
    return read_input


def main():
    """Flow of solution"""
    input_string = read_file('./input.txt')
    print(input_string)

if __name__ == "__main__":
    # If you want to use python debugging uncomment the following line
    # You will also have to provide the correct path
    # change_dir()
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print("Total time: ", end - start)
