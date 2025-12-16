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

def comp_strs(str_a, str_b):
    match = False
    len_a = len(str_a)
    len_b = len(str_b)

    if len_a != len_b:
        print("bad match")
        return match

    for partition in range(1, len_a + 1):
        test_str_a = str_a[:partition - 1] + str_a[partition:]
        test_str_b = str_b[:partition - 1] + str_b[partition:]
        if test_str_a == test_str_b:
            match = test_str_a
            break

    return match

def brute_force_it(id_list):
    current_counter = 0
    ret_str = ""

    while ret_str == "":
        current = id_list[current_counter]
        for comp_id in id_list[current_counter + 1 : ]:

            test_comp = comp_strs(current, comp_id)
            if test_comp:
                ret_str = test_comp
                break

        current_counter += 1

    return ret_str


def main():
    """Flow of solution"""
    fake_tab = f'{" ":^5}'
    file_in = './input.txt'
    input_string = read_file(file_in)
    # print(input_string)
    in_list = input_string.splitlines()

    total = brute_force_it(in_list)
    print(f'Part 2 {fake_tab} Input: {file_in} {fake_tab} Solution: {total} ')


if __name__ == "__main__":
    # If you want to use python debugging uncomment the following line
    # You will also have to provide the correct path
    change_dir()
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print("Total time: ", end - start)
