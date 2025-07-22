import random

from PIL import Image, ImageDraw

rand = random.SystemRandom(0)

width = 32
n = 5
size = width * n * 3
directions = [[-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0]]
datas = [
        [rand.choice([0, 1]), rand.choice([0, 1]), rand.choice([0, 1]), rand.choice([0, 1]),
         rand.choice([0, 1]), rand.choice([0, 1]), rand.choice([0, 1]), rand.choice([0, 1])]
        for x in range(n)
        for y in range(n)]

img = Image.new(mode="RGB", size=(size, size), color=(255, 255, 255))
draw = ImageDraw.Draw(img)
x = 1
y = 1
for data in datas:
    draw.rectangle( (width * x, width * y, width * x + width, width * y + width ),
                    fill=(0, 0, 0))
    for d in range(len(data)):
        if data[d] == 0:
            color = (255, 0, 0)
        else:
            color = (0, 0, 255)
        draw.rectangle((
            width * (x + directions[d][0]), width * (y + directions[d][1]),
            width * (x + directions[d][0] + 1), width * (y + directions[d][1] + 1)
        ), fill=color)
    draw.rectangle((width * (x - 1), width * (y - 1), width * (x + 2), width * (y + 2)),
                   outline=(0, 0, 0), width=3)
    x += 3
    if x > 3 * n:
        x = 1
        y += 3
img.save("field.png", format="PNG")
