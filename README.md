# Citizen Services (CITZ) Information Management Branch (IMB) Full Stack Developer (FSD) Duck Quest (DQ)

## Overview

This repository will be used to hold the problem overview and sample data for IMB FSD's Duck Quest.

As new days are added please update this readme with information on what has been done to ease the process of finding new problems.

## Disclamer

The problems in this repository have been greatly influenced by or modified from:

- [Advent of Code](https://adventofcode.com)
- [Everybody Codes](https://everybody.codes/home)

The problems in this repository are not created or owned by the developers in CITZ IMB.

## Day Breakdown

|           | Status               | Name                           | Path                                       | Overview                                                                                                         |
| :-------: | -------------------- | ------------------------------ | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| :star:    | SOLVED Sept 10, 2024 | Appartment Directions          | `./day1-appartment-floor-directions`       | Given direction input (one line of text "(" go up a floor. ")" go down a floor) determine what floor you end on. |
| :star:    | SOLVED Sept 17, 2024 | Appartment Directions (part 2) | `./day2-appartment-floor-directions-part2` | Given input (same as Appartment Directions) determine what step places you on floor '-1' for the first time.     |
| :star:    | SOLVED Sept 24, 2024 | City Grid Directions           | `./day3-city-grid-directions`              | Given direction input determine the distance from your starting position to your final position.                 |
| :star:    | SOLVED Nov 12, 2024  | Sum Repeating Numbers          | `./day4-sum-repeating-digits`              | Sum all digits in input that match the first digit.                                                              |
| :pushpin: | UNSOLVED             | Frequency Change               | `./day5-frequency-change`                  | Given frequency and change(s) as input determine the resulting frequency.                                        |


## Adding New Day

To add a new problem follow these steps:

1. Copy the `./template-day` folder
2. Rename the folder with the following pattern `day<X>-<brief-description>`
    1. Where `<X>` represents the next number of day that hasn't yet been created
    2. Where `<brief-description>` represents a 2-5 word description of the problem
3. Update the `overview.md` to hold the new problem information
4. Add a `input.txt` file to hold the new problem's input
    - Note: This file should NOT be added to the public repository.
5. Update this README with information on the new problem
6. Templates for easily reading in `input.txt` have been added to the `template-day` for Python and JavaScript.
