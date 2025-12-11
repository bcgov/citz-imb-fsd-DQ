# Quick Overview

Imagine you are watching a device that is tracking changes in frequency. You make a list of changes.
Assume the starting frequency is 0.
Frequencies are listed as `<+/->N` where:
  - `+` indicates that the frequency has increased by N
  - `-` indicates that the frequency has decreased by N
  - N is a whole number

### Disclaimer

This problem was heavily influenced by the [Advent of Code 2018 day 1](https://adventofcode.com/2018/day/1) problem.

# Question

Find the first frequency that the device lands on twice. You may need to loop through the input multiple times to find a repeated frequency.

## Examples:

1. `+1, -2, +3, +1` -> `2`
    - Starting from `0`  we update with `+1` -> `1`
    - Starting from `1`  we update with `-2` -> `-1`
    - Starting from `-1` we update with `+3` -> `2`
    - Starting from `2`  we update with `+1` -> `3`
    - Starting from `3`  we update with `+1` -> `4`
    - Starting from `4`  we update with `-2` -> `2`
    - `2` is the first frequency we have seen twice and our answer
2. `+1, +1, -2` -> `0`
   - `0` `+1` = `1`
   - `1` `+1` = `2`
   - `2` `-2` = `0`
