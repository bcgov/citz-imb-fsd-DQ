"""Used as the solution for the 8th day in python"""

import time
import os

def change_dir():
    """For python debugging"""
    os.chdir("/Users/tafriese/code/citz-imb-fsd-DQ/day8-find-id")

def read_file(file_path):
    """Used to read a files content and return said content"""
    read_input = ''
    with open(file_path, "r", encoding="utf-8") as file:
        read_input = file.read()
    return read_input


def main():
    """Flow of solution"""
    fake_tab = f'{" ":^5}'
    file_in = './test.txt'
    input_string = read_file(file_in)
    # print(input_string)
    in_list = input_string.splitlines()


    # print(f'Part 2 {fake_tab} Input: {file_in} {fake_tab} Solution: {total} ')


if __name__ == "__main__":
    # If you want to use python debugging uncomment the following line
    # You will also have to provide the correct path
    change_dir()
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print("Total time: ", end - start)
