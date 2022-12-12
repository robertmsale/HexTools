#!/usr/bin/python3
import json
import sys
import re


def createAlfredObject(title, subtitle, arg):
    return {
        'title': title,
        'subtitle': subtitle,
        'arg': arg,
        'text': {
            'copy': arg
        }
    }


def createAlfredJSON(items):
    return json.dumps({'items': items}, indent=4)


def parse(s):
    if s[0:2] == "0b":
        return int(s, 2)
    elif s[0:2] == "0x":
        return int(s, 16)
    elif s[0:2] == "0o":
        return int(s, 8)
    else:
        return int(s)


def createFromInt(num):
    strings = [str(num), hex(num), bin(num), oct(num)]
    subtitles = ["Decimal", "Hex", "Binary", "Octal"]
    retval = []
    for i in range(0, len(strings)):
        retval.append(createAlfredObject(strings[i], subtitles[i], strings[i]))
    return createAlfredJSON(retval)


if len(sys.argv) == 1 or False:
    sys.stdout.write(createAlfredJSON([createAlfredObject(sys.argv[1], "enter some kind of number to continue", "")]))
    exit(0)

operators = set("+-*/")
args = sys.argv[1]
numsiter = re.findall(r'0b[01]+|0x[0-9a-fA-F]+|0o[0-7]+|\d+', args)
opsiter = re.findall(r'[+\-*/]', args)
nums = []
ops = []
for i in numsiter:
    nums.append(parse(i))
    nums.append(0)

for i in opsiter:
    ops.append("")
    ops.append(i)

if len(nums) == 0:
    sys.stdout.write(createAlfredJSON(
        [createAlfredObject("No numbers found", "make sure the number(s) are being typed correctly", "")]))
    exit(0)

if len(nums) == 2:
    sys.stdout.write(createFromInt(nums[0]))
    exit(0)

acc = nums[0]
for i in range(1, len(ops), 2):
    if i >= len(nums)-1:
        break
    parsed = nums[i+1]
    if ops[i] == "+":
        acc += parsed
    elif ops[i] == "-":
        acc -= parsed
    elif ops[i] == "*":
        acc *= parsed
    else:
        acc /= parsed

sys.stdout.write(createFromInt(acc))