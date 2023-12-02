import re

VALUES = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

PATTERN = r"(?=(" + "|".join(VALUES.values()) + "|" + "|".join(VALUES.keys()) + "))"


def main():
    file1 = open("input.txt", "r")
    Lines = file1.readlines()
    calibrationValue = 0
    for line in Lines:
        calibrationValue += findCalibrationValue(line)
    print(calibrationValue)


def findCalibrationValue(line):
    print(line)
    nb = []
    print(PATTERN)
    matches = re.findall(PATTERN, line)
    print(matches)
    for match in matches:
        if len(match) > 1:
            nb.append(VALUES[match])
        else:
            nb.append(match)

    return int(nb[0] + nb[len(nb) - 1])


main()
