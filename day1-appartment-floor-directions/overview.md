# Quick Overview

You are lost in an appartment building. There are directions but they are written strangely.
The building has no perceivable top or bottom floor (assume it goes from negative infinity to positive infinity.)

An open bracket '(' in the directions indicates you should go up a floor. A closing bracket ')' in the instructions means you should go down a floor. 

### Disclamer

This problem was heavily influenced by the [Advent of Code 2015 day 1](https://adventofcode.com/2015/day/1) problem. 

## Examples: 

- (()) and ()() both result in floor 0.
- ((( and (()(()( both result in floor 3.
- ))((((( also results in floor 3.
- ()) and ))( both result in floor -1 (the first basement level).
- ))) and )())()) both result in floor -3.

# Question

If you start at floor 0 and go through all the instructions found in input.txt what floor will you end up at? 
