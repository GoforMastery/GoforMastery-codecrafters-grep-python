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


def positiveCharGroup(given, goal):
    # check if you find given in goal.
    # it acts like c++ unordered_map<char, bool> mp.
    umap = {}
    glen = len(goal)
    for idx in range(1, glen - 1):
        umap[goal[idx]] = True
    for c in given:
        if umap[c] == True:
            return True
    return False


# why my code is not working i dont know!
def negativeCharGroup(given, goal):
    umap = {}
    for c in goal:
        umap[c] = True
    for char in given:
        if char not in umap:
            return True
    return False


def checkonlyBraces(pattern):
    length = len(pattern)
    return pattern[0] == "[" and pattern[length - 1] == "]" and pattern[1] != "^"


def checkArrow(pattern):
    length = len(pattern)
    return pattern[0] == "[" and pattern[length - 1] == "]" and pattern[1] == "^"


def containsThis(pattern):
    return "\\w" in pattern or "\\d" in pattern


def containsArrow(pattern):
    for ch in pattern:
        if ch == "^":
            return True
    return False


def checkArrowfromStart(input_line, pattern):
    if len(pattern) > len(input_line):
        return False
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] != input_line[j]:
            return False
        else:
            i = i + 1
            j = j + 1
    return True


def findthem(input_line, pattern):
    i = 0
    j = 0
    ps = len(pattern)
    while j < len(input_line):
        if i < ps - 1 and pattern[i] == "\\" and pattern[i + 1] == "d":
            if input_line[j].isdigit():
                i += 2
                if i == ps:
                    return True
            else:
                i = 0
        elif i < ps - 1 and pattern[i] == "\\" and pattern[i + 1] == "w":
            if input_line[j].isalpha():
                i += 2
                if i == ps:
                    return True
            else:
                i = 0
        elif i < ps and input_line[j] == " " and pattern[i] == " ":
            i += 1
            if i == ps:
                return True
        elif i < ps and input_line[j] == pattern[i]:
            i += 1
            if i == ps:
                return True
        else:
            i = 0

        j += 1

    return False


def findThis(input_line, pattern):
    # i feel i can use two pointers and sliding window
    umap = {}
    nmap = {}
    for ch in pattern:
        if containsAlpha(ch):
            umap[r"\w"] = umap.get(r"\w", 0) + 1
        elif containsDigit(ch):
            umap[r"\d"] = umap.get(r"\d", 0) + 1
        elif ch == " ":
            umap[" "] = umap.get(" ", 0) + 1
    i = 0
    j = 0

    while j < len(input_line):
        if containsAlpha(input_line[j]):
            nmap[r"\w"] = nmap.get(r"\w", 0) + 1
        elif containsDigit(input_line[j]):
            nmap[r"\d"] = nmap.get(r"\d", 0) + 1
        elif input_line[j] == " ":
            nmap[" "] = nmap.get(" ", 0) + 1

        if j - i + 1 < len(pattern):
            j = j + 1
        elif j - i + 1 == len(pattern):
            if umap == nmap:
                k = i
                p = 0
                q = k + len(pattern)
                while k < q:
                    check = True
                    if input_line[k] != pattern[p]:
                        check = False
                        break
                    k = k + 1
                    p = p + 1
                if check == True:
                    return True
            if containsAlpha(input_line[i]):
                nmap[r"\w"] -= 1
            elif containsDigit(input_line[i]):
                nmap[r"\d"] -= 1
            elif input_line[i] == " ":
                nmap[" "] -= 1

            i = i + 1
            j = j + 1

    return False


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    elif findThis(input_line, pattern):
        return findThis(input_line, pattern)
    elif pattern == r"\d":
        return containsDigit(input_line)
    elif pattern == r"\w":
        return validWord(input_line)
    elif checkonlyBraces(pattern):
        return positiveCharGroup(input_line, pattern)
    elif checkArrow(pattern):
        return negativeCharGroup(input_line, pattern)
    elif containsThis(pattern):
        return findthem(input_line, pattern)
    elif containsArrow(pattern):
        return checkArrowfromStart(input_line, pattern)
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()
    # print("debugging")
    # print(sys.argv[0])
    # print(sys.argv[1])
    # print(sys.argv[2])
    # print("debugging ended")
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
