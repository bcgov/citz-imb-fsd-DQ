"""Used as the solution for the fifth day in python"""
import os
import time

def change_dir():
    """For python debugging"""
    os.chdir("/Users/tafriese/code/citz-imb-fsd-DQ/day5-frequency-change")

# # pylint: disable=wrong-import-position
# from utils import read_file
# # pylint: enable=wrong-import-position

def read_file(file_path):
    """Used to read a files content and return said content"""
    read_input = ''
    with open(file_path, "r", encoding="utf-8") as file:
        read_input = file.read()
    return read_input.strip()

def main():
    """Flow of solution"""
    input_string = read_file('./test.txt')
    print(input_string)

if __name__ == "__main__":
    change_dir()
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print("Total time: ", end - start)
