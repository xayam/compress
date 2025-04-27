import sys

from c.fold import *

class Fold:
    width = 3
    dataset = []
    state = []
    recovery = []

    def __init__(self):
        pass

    def init(self, data):
        self.dataset = [d for d in data]

    def encode(self, data):
        self.init(data=data)
        print(self.dataset)
        self.state.append(self.dataset)
        for y in range(1, self.width):
            x = []
            for i in range(self.width - y):
                x.append(self.state[-1][i + 1] - self.state[-1][i])
            self.state.append(x)
        return self.state[-1][0]

    def decode(self, data):
        print(data)
        self.recovery_expand(data=[[data]])
        return data

    def recovery_expand(self, data, depth=1):
        size = (abs(data[-1][0]) + 1) // 2 + 1
        # print("size=" + str(size))
        if depth == 20 * self.width:
            # print(data)
            return data
        self.recovery.append(data)
        current = data[-1]
        for curr in current:
            print(curr)
            row = []
            for x in range(-size, size + 1):
                y = curr + x
                if current != [x, y]:
                    row.append([x, y])
            for variant in row:
                datas = data[:]
                datas.append(variant)
                print(datas)
                return self.recovery_expand(data=datas, depth=depth + 1)
        return None

    def save(self, filename):
        pass

    def get_input(self, filename="input.txt"):
        with open(filename, mode="rb") as f:
            text = f.read()
        count = -1
        for byte in text:
            count += 1
            if count < self.width:
                yield byte
            else:
                break

    def get_random(self):
        choice_list = [0, 1, 2]  # list(range(2 ** 8))
        for i in range(self.width):
            value = rand.choice(choice_list)
            yield value


def main():
    f = Fold()
    compress = f.encode(data=f.get_random())
    decompress = f.decode(data=compress)
    # assert f.dataset == decompress

if __name__ == "__main__":
    main()
