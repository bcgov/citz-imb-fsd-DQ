"""Used as the solution for the fifth day in python"""
import os
import time

def change_dir():
    os.chdir("/Users/tafriese/code/citz-imb-fsd-DQ/day6-frequency-change-part2")

# # pylint: disable=wrong-import-position
# from utils import read_file
# # pylint: enable=wrong-import-position

def read_file(file_path):
    """Used to read a files content and return said content"""
    read_input = ''
    with open(file_path, "r", encoding="utf-8") as file:
        read_input = file.read()
    return read_input.strip()

"""

PART 2

solutions:
  - small.txt 10
  - med.txt
  - input.txt 549

code:
  - add loop function and parse function
  - split on new line
  - call loop from main

"""
def parse_freq_list(freq: int, in_freq: str):
    temp = int(freq)

    operator = in_freq[0]
    delta = int(in_freq[1:])

    if operator == "+":
        freq += delta
    elif operator == "-":
        freq -= delta

    # print(temp , operator, delta, "=", freq)
    # input()

    return freq

def loop(freq_list: list):
    found_freq = [0]
    cur_freq = 0
    rep_freq = None

    while rep_freq is None:
        for delta_freq in freq_list:
            cur_freq = parse_freq_list(cur_freq, delta_freq)

            if cur_freq in found_freq:
                rep_freq = cur_freq
                break

            found_freq.append(cur_freq)

    return rep_freq

def main():
    """Flow of solution"""
    change_dir()

    input_from = './input.txt'
    input_string = read_file(input_from)
    #print(input_string)
    input_li = input_string.split("\n")

    # PART 2 SOLUTION
    part_2_sol = loop(input_li)
    print(f"Part 2: with input: {input_from}\n\t{part_2_sol:^10}")

if __name__ == "__main__":
    change_dir()
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print("Total time: ", end - start)
