import random

from PIL import Image, ImageDraw

rand = random.SystemRandom(0)

size = 2
l256 = list(range(256))
data = [
    [rand.choice(l256), rand.choice(l256)]
    for x in range(size) for y in range(size)
]

img = Image.open("input.png", mode="r")
draw = ImageDraw.Draw(img)
bin = ""
# for x in range(img.width):
#     for y in range(img.height):
#         point = img.getpixel((x, y))
#         r, g, b = point[0], point[1], point[2]
#         bin += format(r, '08b') + format(g , '08b') + format(b, '08b')
#         draw.point((x, y),  fill=(r, g, b))
# img.save("output/000.png", format="PNG")
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
