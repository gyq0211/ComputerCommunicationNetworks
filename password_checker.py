# Project 2 Program 2 Password Checker
# version python 3.8
import re
from itertools import groupby


# Returns sequence if found, empty list otherwise
def consecutive_number(s):
    pos = 0
    stack = []
    while pos != len(s):
        try:
            val = int(s[pos])
        except ValueError:
            pos += 1
            stack = []
            continue
        if not stack:
            stack.append(val)
        elif stack[-1] + 1 == val:
            stack.append(val)
            if len(stack) == 4:
                return stack
        else:
            stack = []
        pos += 1
    return []


def consecutive_letter(pw):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    inp_lower = pw.lower()
    for idx in range(0, len(inp_lower) - 4):
        test_seq = inp_lower[idx:idx + 5]
        if test_seq in alphabet:
            return True


while True:
    password = input("Enter a password: ")
    if len(password) < 8:
        print("Make sure your password is at lest 8 letters")
    elif re.search('[0-9]', password) is None:
        print("Make sure your password has a number in it")
    elif re.search('[a-zA-Z]', password) is None:
        print("Make sure your password has a letter in it")
    elif any((len(list(val)) > 4) for (char, val) in groupby(password)):
        print('Password cannot contains 5 consecutive repetitive character')
    elif consecutive_number(password):
        print("Password cannot contains 5 or more consecutive numbers")
    elif consecutive_letter(password):
        print("Password cannot contains 5 or more consecutive letters")
    else:
        print("Your password is valid.")
        break
