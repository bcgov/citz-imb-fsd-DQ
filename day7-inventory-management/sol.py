"""Used as the solution for the 7th day in python"""

import time
import os

def change_dir():
    """For python debugging"""
    os.chdir("/Users/tafriese/code/citz-imb-fsd-DQ/day7-inventory-management")

def read_file(file_path):
    """Used to read a files content and return said content"""
    read_input = ''
    with open(file_path, "r", encoding="utf-8") as file:
        read_input = file.read()
    return read_input

def tally_repeats(id_list):
    two_rep_count = 0
    three_rep_count = 0

    for cur_id in id_list:
        if cur_id == "":
            continue
        id_chars = {}
        for char in cur_id:
            if char == " ":
                continue
            if char not in id_chars.keys():
                id_chars[char] = 1
            else:
                id_chars[char] += 1

        found_double = False
        found_triple = False

        for k_v_pair in id_chars.items():
            # key = k_v_pair[0]
            value = k_v_pair[1]
            if value == 2 and not found_double:
                two_rep_count += 1
                found_double = True
                continue
            if value == 3 and not found_triple:
                three_rep_count += 1
                found_triple = True

    return two_rep_count * three_rep_count


def main():
    """Flow of solution"""
    fake_tab = f'{" | ":^5}'
    file_in = './input.txt'
    input_string = read_file(file_in)
    # print(input_string)
    in_list = input_string.splitlines()
    total = tally_repeats(in_list)
    print(f'Part 1 {fake_tab} Input: {file_in} {fake_tab} Solution: {total} ')


if __name__ == "__main__":
    # If you want to use python debugging uncomment the following line
    # You will also have to provide the correct path
    change_dir()
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print("Total time: ", end - start)
