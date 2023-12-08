def solvePart1(engineScheme):
    sum = 0
    numbersBuffer = ""
    numberValidated = False
    for x in range(len(engineScheme)):
        for y in range(len(engineScheme[x])):
            currentTile = engineScheme[x][y]
            if currentTile.isdigit():
                numbersBuffer += currentTile
                if hasSymbolNeighbor(engineScheme, x, y):
                    numberValidated = True

            else:
                if numberValidated:
                    sum += int(numbersBuffer)
                numbersBuffer = ""
                numberValidated = False

            if y == len(engineScheme[x]) - 1:
                if numberValidated:
                    sum += int(numbersBuffer)
                numbersBuffer = ""
                numberValidated = False
    print("Part1 Sum : " + str(sum))


def solvePart2(engineScheme):
    sum = 0
    numbersBuffer = ""
    numberValidated = False
    starSymbols = {}
    lastStar = ""
    for x in range(len(engineScheme)):
        for y in range(len(engineScheme[x])):
            currentTile = engineScheme[x][y]
            if currentTile.isdigit():
                numbersBuffer += currentTile
                neighbor = starNeighborIfExist(engineScheme, x, y)
                if neighbor:
                    numberValidated = True
                    lastStar = neighbor
                    if not starSymbols.get(neighbor):
                        starSymbols[neighbor] = []
            else:
                if numberValidated:
                    starSymbols[lastStar].append(int(numbersBuffer))
                numbersBuffer = ""
                lastStar = ""
                numberValidated = False

            if y == len(engineScheme[x]) - 1:
                if numberValidated:
                    starSymbols[lastStar].append(int(numbersBuffer))
                numbersBuffer = ""
                lastStar = ""
                numberValidated = False
    for star in starSymbols:
        if len(starSymbols[star]) == 2:
            sum += multiplyList(starSymbols[star])
    print("Part2 Sum : " + str(sum))


def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result


def starNeighborIfExist(mat, row, col, radius=1):
    rows, cols = len(mat), len(mat[0])
    for i in range(row - radius, row + 1 + radius):
        for j in range(col - radius, col + 1 + radius):
            if 0 <= i < rows and 0 <= j < cols and not (i == row and j == col):
                currentTile = mat[i][j]
                if currentTile == "*":
                    return str(i) + "," + str(j)
    return None


def hasSymbolNeighbor(mat, row, col, radius=1) -> bool:
    rows, cols = len(mat), len(mat[0])
    for i in range(row - radius, row + 1 + radius):
        for j in range(col - radius, col + 1 + radius):
            if 0 <= i < rows and 0 <= j < cols and not (i == row and j == col):
                currentTile = mat[i][j]
                if not currentTile.isalnum() and currentTile != ".":
                    return True
    return False


if __name__ == "__main__":
    part1 = open("part1.txt", "r")
    part1Schematic = [list(line.strip()) for line in part1.readlines()]
    solvePart1(part1Schematic)

    part2example = open("part1.txt", "r")
    part2ExampleSchematic = [list(line.strip()) for line in part2example.readlines()]
    solvePart2(part2ExampleSchematic)
