# Quick Overview

Imagine you are watching a device that is tracking changes in frequency. You make a list of changes.
Assume the starting frequency is 0.
Frequencies are listed as `<+/->N` where:
  - `+` indicates that the frequency has increased by N
  - `-` indicates that the frequency has decreased by N
  - N is a whole number

### Disclamer

This problem was heavily influenced by the [Advent of Code 2018 day 1](https://adventofcode.com/2018/day/1) problem.

## Examples:

1. `+1, -2, +3, +1` -> `3`
    - Starting from `0`  we update with `+1` -> `1`
    - Starting from `1`  we update with `-2` -> `-1`
    - Starting from `-1` we update with `+3` -> `2`
    - Starting from `2`  we update with `+1` -> `3`
2. `+1, +1, +1` -> `3`
3. `+1, +1, -2` -> `0`
4. `-1, -2, -3` -> `-6`


# Question

Taking in the list of changes determine the result frequency.
