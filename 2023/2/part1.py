RULES = {"red": 12, "green": 13, "blue": 14}


def isGamePossible(game):
    gameElements = game.split(":")
    gameId = int(gameElements[0].split()[1])
    inlineSets = gameElements[1]
    sets = inlineSets.split(";")
    print(sets)
    for set in sets:
        numberAndColor = set.split(",")
        for element in numberAndColor:
            value = element.split()
            nb = int(value[0])
            color = value[1]
            if RULES[color] < nb:
                return 0
    return gameId


if __name__ == "__main__":
    file1 = open("input.txt", "r")
    Lines = file1.readlines()
    idsSum = 0
    for line in Lines:
        idsSum += isGamePossible(line)
    print(idsSum)
