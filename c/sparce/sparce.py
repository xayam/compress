import sys

from PIL import Image, ImageDraw

from c.sparce import *


class Sparce:
    size = 2 ** 8
    width = 2 ** 7
    scheme = {
        0: [1, 0],
        1: [0, None],
    }
    inner = []
    img = None
    draw = None
    additions = []
    recovery = []
    dataset = None
    results = []
    counts = [2]
    state = None

    def __init__(self):
        self.init()

    def init(self):
        # print(1)
        self.spiral_init(n=2 * self.size - 1)
        # print(2)
        self.img = Image.new(mode="1", size=(self.size, self.size), color=0)
        self.draw = ImageDraw.Draw(self.img)

    def encode(self, data):
        print("Start compress...")
        self.dataset = []
        self.additions = []
        result = []
        count = 0
        curr = 1
        dx, dy = 0, 0
        # print("#1")
        p0, p1, p2, p3, p4, p5 = self.spiral(position=curr)
        x_curr, y_curr, dx1, dy1, dx2, dy2 = p0, p1, p2, p3, p4, p5
        v = data.__next__()
        x_two = self.size // 2
        if v == 0:
            y_two = self.size // 2 - 1
        else:
            y_two = self.size // 2 - 2
        self.dataset.append(v)
        result.append((x_two, y_two))
        self.additions.append({"x": x_two, "y": y_two, "v": v})
        # print("#1", x_curr, x_curr, v)
        while True:
            try:
                value = data.__next__()
                count += 1
                self.progress(f"Compressing: {count + 1}/{self.width}")
            except StopIteration:
                break
            self.dataset.append(value)
            # print("#2", x_curr, y_curr, dx1, dy1, dx2, dy2, curr, value)
            if self.space([y_curr + dy1, x_curr + dx1]) == value:
                dx, dy = p2, p3
                curr = self.spiral(
                    value=[x_curr + 2 * dx1, y_curr + 2 * dy1],
                    position=curr
                )
                p0, p1, p2, p3, p4, p5 = self.spiral(position=curr)
                _, _, dx1, dy1, dx2, dy2 = p0, p1, p2, p3, p4, p5
                # print("#3", dx, dy, dx1, dy1, curr, x_curr, y_curr)
            elif self.space([y_curr + dy1 + dy2, x_curr + dx1 + dx2]) == value:
                dy = p3 + p5
                dx = p2 + p4
                curr = self.spiral(
                    value=[x_curr + 2 * (dx1 + dx2), y_curr + 2 * (dy1 + dy2)],
                    position=curr
                )
                p0, p1, p2, p3, p4, p5 = self.spiral(position=curr)
                _, _, dx1, dy1, dx2, dy2 = p0, p1, p2, p3, p4, p5
                # print("#4", dx, dy, dx1, dy1, dx2, dy2, curr, x_curr, y_curr)
            else:
                raise Exception("Error 401")
            # print("#5", x_two, y_two, dx, dy, value, sep= ", ")
            x_curr = x_curr + 2 * dx
            y_curr = y_curr + 2 * dy
            x_two = x_two + dx
            y_two = y_two + dy
            # print("#6", x_curr, y_curr, x_two, x_two, dx, dy, value)
            result.append((x_two, y_two))
            self.additions.append({"x": x_two, "y": y_two, "v": value})
            self.draw.point((x_two, y_two), fill=1)
            self.img.save("compress.png", format="PNG")
        print("")
        return result

    def decode(self, data):
        print("Start decompress...")
        # print(len(data))
        self.spiral_init(n=2 * self.size - 1)
        recovery = []
        curr = 0
        x_curr, y_curr, _, _, _, _ = self.spiral(position=curr)
        x_two, y_two = data[curr]
        v = 1 if y_two % 2 == 0 else 0
        curr += 1
        recovery.append(v)
        # print("#1", x_curr, y_curr, x_two, y_two, v)
        for _ in range(1, self.width):
            dx = data[curr][0] - data[curr - 1][0]
            dy = data[curr][1] - data[curr - 1][1]
            value = self.space([y_curr + dy, x_curr + dx])
            recovery.append(value)
            x_curr = x_curr + 2 * dx
            y_curr = y_curr + 2 * dy
            x_two = x_two + dx
            y_two = y_two + dy
            # print("#2", dx, dy, x_curr, y_curr, x_two, y_two, value)
            curr += 1
            self.progress(f"Decompressing: {curr}/{self.width}")
        print("")
        self.decode_save(recovery)
        return recovery

    @staticmethod
    def sign(value):
        return 1 if value >= 0 else -1

    def spiral_init(self, n):
        self.n = n
        if self.n == 0:
            return []
        self.x = self.y = self.n // 2
        self.result = [[self.x, self.y]]
        self.directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        self.current_dir = 0
        self.step_size = 1
        self.dir_changes = 0
        self.current = [self.result[0][0], self.result[0][1], 0, 0, 0, 0]
        self.result2 = {0: self.current}
        self.pos = 1
        self.index = 0
        self.ss = 0
        self.v = 1
        self.count = 1
        self.last_del = -1
        self.route = dict()
        self.route[0] = 1
        self.route[1] = 0
        self.route_index = 2
        self.route_last_del = -1
        self.d = 0
        self.spiral_expand()
        return None

    def route_expand(self):
        for i in range(self.route_last_del + 1, self.route_index - 2 * self.count):
            self.route.__delitem__(i)
            self.route_last_del = i
        for i in range(2):
            self.count += 1
            self.d += 1
            self.v += 1
            if self.d > 3:
                self.d = 0
            for _ in range(self.count):
                self.route[self.route_index] = self.d
                self.route_index += 1
            self.d += 1
            if self.d > 3:
                self.d = 0
            for _ in range(self.count):
                self.route[self.route_index] = self.d
                self.route_index += 1

    def space(self, position):
        x, y = position
        result = self.scheme[x % 2][y % 2]
        return result

    @staticmethod
    def decode_save(recovery, filename="decompress.txt"):
        # print(self.dataset)
        # print(recovery)
        recovery = "".join(map(str, recovery))
        with open(filename, mode="w", encoding="windows-1251") as f:
            for i in range(0, len(recovery), 8):
                char = bytes([int(recovery[i: i + 8] , 2)]).decode(
                    "windows-1251", errors="ignore"
                )
                f.write(char)

    def encode_phase2(self):
        img2 = Image.new(mode="1", size=(self.size, self.size), color=0)
        draw2 = ImageDraw.Draw(img2)
        for r in range(len(self.results)):
            for i in range(len(self.results[r])):
                self.results[r][i] = \
                    self.results[r][i][0] - i // 2.5, self.results[r][i][1]
                draw2.point(self.results[r][i], fill=1)
        img2.save("compress2.png", format="PNG")

    @staticmethod
    def has_element(arr1, arr2):
        set_arr2 = set(tuple(point) for point in arr2)
        for point in arr1:
            if tuple(point) in set_arr2:
                return True
        return False

    def get_random(self):
        for _ in range(self.width):
            value = rand.choice([0, 1])
            yield value

    def get_input(self, filename="input.txt"):
        with open(filename, mode="rb") as f:
            text = f.read()
        count = -1
        for byte in text:
            binary_str = bin(byte)[2:].zfill(8)
            for binary in binary_str:
                count += 1
                if count < self.width:
                    yield int(binary)
                else:
                    break

    # def spiral_scan(self, current, value):
    #     # print(self.result2)
    #     # print(value)
    #     for i in range(len(self.result2)):
    #         # print(i)
    #         if (self.spiral(i)[0] == value[0]) and (self.spiral(i)[1] == value[1]):
    #             return i
    #     return None

    def spiral_expand(self):
        count = 0
        dirs = 1
        self.result = self.result[-1:]
        for i in range(self.last_del + 1, self.pos - 1):
            self.result2.__delitem__(i)
            self.last_del = i
        while len(self.result) < self.n * self.n:
            for ss in range(self.step_size):
                dx, dy = self.directions[self.current_dir]
                new_x = self.result[-1][0] + dx
                new_y = self.result[-1][1] + dy
                if 0 <= new_x < self.n and 0 <= new_y < self.n:
                    self.result.append([new_x, new_y])
                    count += 1
                    if len(self.result) == self.n * self.n:
                        break
            if len(self.result) == self.n * self.n:
                break
            self.current_dir = (self.current_dir + 1) % 4
            dirs += 1
            self.dir_changes += 1
            if self.dir_changes % 2 == 0:
                self.step_size += 1
            if dirs > 4:
                break
        return self.spiral_update(count=count)

    def spiral_update(self, count):
        if count == 0:
            return None
        self.route_expand()
        i = 0
        for point in self.result[1:]:
            i += 1
            dx, dy = point[0] - self.current[0], point[1] - self.current[1]
            self.current = [
                self.current[0], self.current[1],
                dx, dy,
                self.directions[self.route[self.index]][0],
                self.directions[self.route[self.index]][1]
            ]
            if (0 > self.current[0]) or (self.current[0] >= self.n) or \
                    (0 > self.current[1]) or (self.current[1] >= self.n):
                return None
            self.result2[self.pos] = self.current[:]
            self.current = point[:]
            self.index += 1
            self.pos += 1
        return None

    def spiral(self, value=None, position=None):
        if value is not None:
            i = position
            while True:
                point = self.spiral(position=i)
                if (point[0] == value[0]) and (point[1] == value[0]):
                    return i
                i += 1
        elif position is not None:
            while True:
                try:
                    return self.result2[position]
                except KeyError:
                    self.spiral_expand()
        return None

    @staticmethod
    def progress(message: str) -> None:
        sys.stdout.write("\r" + message)
        sys.stdout.flush()

def main():
    s = Sparce()
    compress = s.encode(data=s.get_random())
    decompress = s.decode(compress)
    # print(s.dataset)
    # print(decompress)
    assert s.dataset == decompress


if __name__ == "__main__":
    main()
