# Quick Overview

Review a sequence of digits (whole numbers.) Find the sum of all digits that match the digit following the first in the list.
The list is circular, so the digit after the last digit is the first digit in the list.

### Disclamer

This problem was heavily influenced by the [Advent of Code 2017 day 1](https://adventofcode.com/2017/day/1) problem.

## Examples:

- `1122`        produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
- `1111`        produces 4 because each digit (all 1) matches the next.
- `1234`        produces 0 because no digit matches the next.
- `91212129`    produces 9 because the only digit that matches the next one is the last digit, 9.

# Question

 What is the sum of all the repeating digits?
