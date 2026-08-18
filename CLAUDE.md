# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

This repository is a collection of standalone Python scripts. There is no unified build system or test suite.

- **Run a solution**: `python <path_to_file>.py`
- **Run a specific test (if present in file)**: Most files contain their own test cases in the `if __name__ == "__main__":` block; run the file directly.

## Code Architecture

The codebase is organized by the source of the programming challenges:

- `lc150/`: Solutions for the "LeetCode 150" list, organized by algorithmic category:
    - `array_hashing/`
    - `binary_search/`
    - `linked_list/`
    - `stack/`
    - `tree/`
    - `two_pointers/`
    - `graph/`
    - `backtracking/`
- `epi/`: Solutions from "Elements of Programming Interviews", organized by chapter:
    - `c4/` (e.g., basic data structures, simple algorithms)
    - `c5/` (e.g., arrays)
