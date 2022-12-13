# HexTools for Alfred

![example](https://raw.githubusercontent.com/robertmsale/HexTools/main/example.gif)

## Description

This is an Alfred workflow that allows you to convert between hex, decimal, binary and octal. It uses Python3 so you must have the latest MacOS release.

Also supports basic arithmetic from left to right (no operator precedence)

## Roadmap

- Implement operator precedence
- Implement binary operators (&, |, <<, >>, ~, etc)
- Implement parsing of expression trees
  - i.e. `(x = 0b1101, x * 0xff) # evaluates to 3315`
- Make the script pick whichever python3 interpreter is installed to `$PATH`
  - the main script will use bash/zsh
  - it will load script.py into a string
  - it will pass that whole script as a string into python3
  - this will allow the script to use `which python3` to find your python3 interpreter

## Install

Download the latest release from the Releases section, open up Alfred workflow preferences and import the downloaded workflow file.

## Special considerations

The latest version of MacOS ships with Python3, but if you want to use another Python3 interpreter installed in another location you have to change the crunch-bang `#!` directive at the top of the file to the path of your Python3 interpreter.

Alfred has a limitation where it only lets you select from a few built in interpreters and shells. The plan is to eventually make HexTools MacOS version agnostic. 