import random

rand = random.SystemRandom(0)

size = 2
list256 = list(range(256))
data = [
    [rand.choice(list256), rand.choice(list256)]
    for x in range(size) for y in range(size)
]

bin = ""

directions = [
    [2, 3, 5, 6],
    [1, 3, 4, 6],
    [1, 2, 4, 5],
    [2, 3, 5, 6],
    [1, 3, 4, 6],
    [1, 2, 4, 5],
]
state = [True] * 6
summa = 0
result = []

def search(state, current, path, count=0):
    global summa
    global directions
    global result
    for direction in range(4):
        index = directions[current][direction] - 1
        if state[index]:
            moves = state[:]
            moves[index] = False
            way = path[:]
            way.append(index)
            search(state=moves, current=index, path=way, count=count)
    if len(path) == 6:
        summa += 1
        result.append("".join(map(str, path)))
        print(f"path=\"{path}\"")


def main():
    global state
    global result
    for index in range(6):
        moves = state[:]
        moves[index] = False
        search(state=moves, current=index, path=[index])
    print(f"summa=\"{summa}\"")
    print(len(set(result)))


if __name__ == "__main__":
    main()
