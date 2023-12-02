def gamePower(game):
    gameElements = game.split(":")
    inlineSets = gameElements[1]
    sets = inlineSets.split(";")
    print(sets)
    counterByColor = {"red": 0, "green": 0, "blue": 0}
    for set in sets:
        numberAndColor = set.split(",")
        for element in numberAndColor:
            value = element.split()
            nb = int(value[0])
            color = value[1]

            if counterByColor[color] < nb:
                counterByColor[color] = nb
    print(counterByColor)
    power = multiplyList(counterByColor.values())
    print(power)
    return power


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


if __name__ == "__main__":
    file1 = open("input.txt", "r")
    Lines = file1.readlines()
    powerSum = 0
    for line in Lines:
        powerSum += gamePower(line)
    print(powerSum)
