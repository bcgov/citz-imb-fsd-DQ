"""DAY 5 """

import sys
import os
import time

def change_dir():
    os.chdir("/Users/tafriese/code/citz-imb-fsd-DQ/day5-frequency-change")

sys.path.append("..")

def read_file(file_path):
    """Used to read a files content and return said content"""
    read_input = ''
    with open(file_path, "r", encoding="utf-8") as file:
        read_input = file.read()
    return read_input.strip()

"""
PART 1

solutions:
  - small.txt 32
  - input.txt 508

code:
  - convert to list in main()
  - add the following function and a call to it from main
"""
def parse_freq_list_part_1(in_freq: list):
    freq = 0
    for delta_freq in in_freq:
        operator = delta_freq[0]
        delta = int(delta_freq[1:])
        #print("op: ", operator, "delta: ", delta)
        if operator == "+":
            freq += delta
        elif operator == "-":
            freq -= delta
    return freq

def main():
    """Flow of solution"""
    change_dir()

    input_from = './input.txt'
    input_string = read_file(input_from)
    #print(input_string)
    input_li = input_string.split("\n")

    # PART 1 SOLUTION
    part_1_sol = parse_freq_list_part_1(input_li)
    print(f"Part 1: with input: {input_from}\n\t{part_1_sol:^10}")

if __name__ == "__main__":
    change_dir()
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print("Total time: ", end - start)
