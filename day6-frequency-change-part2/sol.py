"""Used as the solution for the fifth day in python"""
import sys
import os
import time
from typing import Set

def change_dir():
    """For python debugging"""
    os.chdir("/Users/tafriese/code/citz-imb-fsd-DQ/day6-frequency-change-part2")

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
    current_value = 0
    loop_counter = 0

    tracker = set()
    tracker.add(0)
    found = False
    while not found:
      loop_counter += 1
      for input_line in input_li:
          # Is positive or negative?
          # string = "abcd"
          # string_1 = string[0 : 3]
          number = int(input_line)
          #print(f"we got {sign:^3} {number:^7} ")
          current_value += number

          if (current_value in tracker):
              print(current_value)
              print(f"Len tracker : {len(tracker)}")
              print(f"Loop counter: {loop_counter}")
              found = True
              break
          else:
              tracker.add(current_value)


if __name__ == "__main__":
    change_dir()
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print("Total time: ", end - start)
