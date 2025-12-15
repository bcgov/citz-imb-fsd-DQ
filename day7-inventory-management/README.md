# Quick Overview

Given a list of inputs you are trying to create a new type of checksum based on repeating characters.
Each line of input will be a string of letter characters (EX: `aabbcc`).

The new checksum can be calculated by counting how many times a character is repeated two or three times then multiplying those numbers together.

In the string above it has 2 letters that appear twice (`a` and `b`) but no characters that appear more than that.

### Disclamer

This problem was heavily influenced by the [Advent of Code 2018 Day 2](https://adventofcode.com/2018/day/2) problem.

## Examples:

1. `abcdef` contains no letters that appear exactly two or three times.
2. `bababc` contains two `a` and three `b`, so it counts for both.
3. `abbcde` contains two `b`, but no letter appears exactly three times.
4. `abcccd` contains three `c`, but no letter appears exactly two times.
5. `aabcdd` contains two `a` and two `d`, but it only counts once.
6. `abcdee` contains two `e`.
7. `ababab` contains three `a` and three `b`, but it only counts once.

Looping through the above examples we would tally the repeating digits in the following way:

```
# Init before looping
double_count = 0 ... triple_count = 0
```
1. `double_count = 0` ... `triple_count = 0`
2. `double_count = 1` ... `triple_count = 1`
3. `double_count = 2` ... `triple_count = 1`
4. `double_count = 2` ... `triple_count = 2`
5. `double_count = 3` ... `triple_count = 2`
6. `double_count = 4` ... `triple_count = 2`
7. `double_count = 4` ... `triple_count = 3`

```
checksum = double_count * triple_count
#                4      *       3      =   12
```

# Question

Parse the input, tally each time a line has a letter that repeats twice or thrice, multiply them together to find the temporary checksum.
