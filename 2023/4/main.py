def solvePart1(cards) -> int:
    total = 0
    for card in cards:
        scorecard = card.split(":")[1].split("|")
        winningNumbers = scorecard[0]
        yourNumbers = scorecard[1]
        nbOfMatch = 0
        score = 0
        for nb in yourNumbers.split():
            if nb in winningNumbers.split():
                if nbOfMatch > 1:
                    score = score * 2
                else:
                    score += 1
                nbOfMatch += 1
        total += score
    return total


def solvePart2(cards) -> int:
    nbOfCardsByIndex = {}
    for idx, card in enumerate(cards):
        cardCounter = nbOfCardsByIndex.get(idx)
        if not cardCounter:
            nbOfCardsByIndex[idx] = 0
        nbOfCardsByIndex[idx] += 1
        scorecard = card.split(":")[1].split("|")
        winningNumbers = scorecard[0]
        yourNumbers = scorecard[1]
        nbOfMatch = 0
        for nb in yourNumbers.split():
            if nb in winningNumbers.split():
                nbOfMatch += 1
        for matched in range(1, nbOfMatch + 1):
            cardCounter = nbOfCardsByIndex.get(idx + matched)
            if not cardCounter:
                nbOfCardsByIndex[idx + matched] = 0
            for _ in range(nbOfCardsByIndex[idx]):
                nbOfCardsByIndex[idx + matched] += 1
    return sum(nbOfCardsByIndex.values())


if __name__ == "__main__":
    example = open("example1.txt", "r")
    exampleCards = [line for line in example.readlines()]

    input = open("input1.txt", "r")
    inputCards = [line for line in input.readlines()]

    print("total example part1 : " + str(solvePart1(exampleCards)))
    print("total input part1 : " + str(solvePart1(inputCards)))
    print("total example part2 : " + str(solvePart2(exampleCards)))
    print("total input part2 : " + str(solvePart2(inputCards)))
