"""Used as the solution for the fifth day in python"""
import sys
import os
import time

def change_dir():
    """For python debugging"""
    os.chdir("/Users/tafriese/code/citz-imb-fsd-DQ/day5-frequency-change")

sys.path.append("..")
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
    input_string = read_file('./input.txt')
    input_li = input_string.splitlines()
    sumNum = 0

    for input_line in input_li:
        # Is positive or negative?
        # string = "abcd"
        # string_1 = string[0 : 3]
        sign = input_line[0]
        number = int(input_line[1:])
        #print(f"we got {sign:^3} {number:^7} ")
        if (sign == "+"):
            sumNum += number
        else:
            sumNum -= number
    print(sumNum)

if __name__ == "__main__":
    change_dir()
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print("Total time: ", end - start)
