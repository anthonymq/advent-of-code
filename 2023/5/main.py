def solvePart1(almanac):
    seeds = almanac[0].split(":")[1].split()
    seedLocation = {}
    seedIsTransformedByCategory = {}
    for seed in seeds:
        seedLocation[int(seed)] = int(seed)
        seedIsTransformedByCategory[int(seed)] = ""
    almanac.pop(0)
    print(seeds)
    almanacMap = {}
    lastAlmanacKey = ""

    for line in almanac:
        if "map" in line:
            lastAlmanacKey = line.split()[0]
            almanacMap[lastAlmanacKey] = {}
        else:
            explodedLine = line.split()
            source = int(explodedLine[1])
            destination = int(explodedLine[0])
            nb = int(explodedLine[2])
            for seed in seedLocation.keys():
                if source <= seedLocation[seed] <= source + nb:
                    if seedIsTransformedByCategory[seed] != lastAlmanacKey:
                        shift = seedLocation[seed] - source
                        seedLocation[seed] = destination + shift
                        seedIsTransformedByCategory[seed] = lastAlmanacKey
    print(almanacMap)
    print(seedLocation)
    print(min(seedLocation.values()))


def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)


def solvePart2(almanac):
    seeds = almanac[0].split(":")[1].split()
    seedRanges = []
    for start, length in pairwise(seeds):
        seedRanges.append((int(start), int(start) + int(length)))
    almanac.pop(0)
    almanacMap = {}
    lastAlmanacKey = ""
    categoryRanges = {}

    for line in almanac:
        if "map" in line:
            lastAlmanacKey = line.split()[0]
            almanacMap[lastAlmanacKey] = {}
        else:
            explodedLine = line.split()
            source = int(explodedLine[1])
            destination = int(explodedLine[0])
            length = int(explodedLine[2])
            if lastAlmanacKey not in categoryRanges.keys():
                categoryRanges[lastAlmanacKey] = []
            categoryRanges[lastAlmanacKey].append((source, destination, length))

    categoryRanges = dict(reversed(categoryRanges.items()))

    location = 0
    while True:
        closestSeed = getSeedByLocation(location, categoryRanges)

        if any(r[0] <= closestSeed < r[1] for r in seedRanges):
            print("seed : " + str(closestSeed))
            print("location : " + str(location))
            break

        location += 1
        if location % 1_000_000 == 0:
            print(location)


def getSeedByLocation(location, categoryRanges):
    seed = location
    for category in categoryRanges:
        # print(categoryRanges[category])
        for categoryRange in categoryRanges[category]:
            source = categoryRange[1]
            nb = categoryRange[2]
            destination = categoryRange[0]
            if source <= seed < source + nb:
                seed = destination + (seed - source)
                # print("location " + str(seed))
                break

        # print(seed)
    return seed


if __name__ == "__main__":
    # example = open("example1.txt", "r")
    # exampleAlmanac = [line.rstrip() for line in example.readlines() if line.rstrip()]
    # solvePart1(exampleAlmanac)
    # input = open("input.txt", "r")
    # inputAlmanac = [line.rstrip() for line in input.readlines() if line.rstrip()]
    # solvePart1(inputAlmanac)

    # example = open("example1.txt", "r")
    # exampleAlmanac = [line.rstrip() for line in example.readlines() if line.rstrip()]
    # solvePart2(exampleAlmanac)
    input = open("input.txt", "r")
    inputAlmanac = [line.rstrip() for line in input.readlines() if line.rstrip()]
    solvePart2(inputAlmanac)
