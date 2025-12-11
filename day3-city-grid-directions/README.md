# Another Direction One

## Overview

Imagine you are standing on a large city grid. You are given directions to your final destination in the form of DX where:
- D = the direction to turn 90 degrees from where you are currently facing and
- X = the number of blocks to walk in that direction.

### Disclaimer

This problem was heavily influenced by the [Advent of Code 2016 day 1](https://adventofcode.com/2016/day/1) problem.

## Question

How far away is the final destination from where you are now?

## Examples

1. L185
    - -> 185 blocks away
    - 185 blocks West
2. R2, L3
    - -> 5 blocks away.
    - 2 blocks East and 3 blocks North
3. R2, R2, R2
    - -> 2 blocks away.
    - 2 blocks East, 2 blocks South, then 2 blocks West leaving you 2 blocks south from where you started.
4. R5, L5, R5, R3
    - -> 12 blocks away
    - East 5 blocks, North 5 blocks, East 5 blocks, then South 3 blocks resulting in you 10 blocks East and North 2 blocks.
