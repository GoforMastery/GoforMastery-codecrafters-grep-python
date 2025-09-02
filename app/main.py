import sys


# import pyparsing - available if you need it!
# import lark - available if you need it!
def isDigit(input_char):
    for ch in "1234567890":
        if ch == input_char:
            return True

    return False


def containsDigit(intput_line):
    for chars in intput_line:
        if isDigit(chars):
            return True
    return False


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif containsDigit(input_line):
        exit(0)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    # print("checking")
    # print(sys.argv[0])
    # print(sys.argv[1])
    # print(sys.argv[2])
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # Uncomment this block to pass the first stage
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
