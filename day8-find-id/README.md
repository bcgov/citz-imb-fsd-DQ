# Quick Overview

Given a list of inputs you are trying to find two lines that differ by only one character. Once the non-matching character is removed the remaining string is the string we are looking for.

### Disclaimer

This problem was heavily influenced by the [Advent of Code 2018 Day 2 Part 2](https://adventofcode.com/2018/day/2) problem.

## Examples:

Given the following list of IDs:

```
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
```

Only `fghij` and `fguij` differ by exactly one character. Our solution in this case is `fgij`.

# Question

Parse the input, find the 'matching' IDs and return the condensed string.
