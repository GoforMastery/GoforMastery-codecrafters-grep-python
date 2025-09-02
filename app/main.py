import sys


# import pyparsing - available if you need it!
# import lark - available if you need it!
def isDigit(input_char):
    for ch in "1234567890":
        if ch == input_char:
            return True

    return False


def isAlpha(input_char):
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch == input_char:
            return True
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ch == input_char:
            return True
    return False


def isUnderScore(input_char):
    return input_char == "_"


def containsDigit(input_line):
    for chars in input_line:
        if isDigit(chars):
            return True
    return False


def containsAlpha(input_line):
    for chars in input_line:
        if isAlpha(chars):
            return True
    return False


def containsUnderScore(input_line):
    for chars in input_line:
        if chars == "_":
            return True
    return False


def validChar(input_char):
    return isDigit(input_char) or isAlpha(input_char) or isUnderScore(input_char)


def validWord(input_line):
    for chars in input_line:
        if validChar(chars):
            return True
    return False


# why my code is not working i dont know!

import sys


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif pattern == r"\d":
        return containsDigit(input_line)
    elif pattern == r"\w":
        return validWord(input_line)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    print("Logs appear here!", file=sys.stderr)

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
